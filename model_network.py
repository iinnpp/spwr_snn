from brian2 import defaultclock, NeuronGroup, Synapses, mV, TimedArray, StateMonitor, PopulationRateMonitor, \
    SpikeMonitor, second, Network, nS, volt, siemens, ms, Hz
import numpy as np
import pickle
import os


def run_net(tr, run_path):
    print('Running the network...')

    netw_objects = []

    # todo change how external input is handled
    data_path = 'D:\\00_modeling\\model_results\\tests\\'
    # file_name = 'ext_input_mult_dict_500ms_2spw'  # 2spw, 500ms
    file_name = 'ext_input_100ms_dt0_1'  # 1spw, 100ms
    with open(data_path + file_name, 'rb') as handle:
        ext_input_dict = pickle.load(handle)

    namespace = tr.netw.f_to_dict(short_names=True, fast_access=True)
    # namespace['idx'] = tr.v_idx not sure why I need that

    defaultclock.dt = tr.netw.sim.dt

    g_chr = TimedArray(ext_input_dict['waveforms'], dt=defaultclock.dt)
    namespace['g_chr'] = g_chr

    ############### SETUP THE NETWORK #####################
    # Neuron populations
    neuron_model_exc = tr.lif_exc
    neuron_model_exc += tr.syn_EE_biexp
    neuron_model_exc += tr.syn_EI_biexp
    namespace['invpeak_E_e'] = (tr.tau_r_E_e / tr.tau_d_E_e) ** (tr.tau_d_E_e / (tr.tau_r_E_e - tr.tau_d_E_e))
    namespace['invpeak_E_i'] = (tr.tau_r_E_i / tr.tau_d_E_i) ** (tr.tau_d_E_i / (tr.tau_r_E_i - tr.tau_d_E_i))

    neuron_model_inh = tr.lif_inh
    neuron_model_inh += tr.syn_II_biexp
    neuron_model_inh += tr.syn_IE_biexp
    namespace['invpeak_I_i'] = (tr.tau_r_I_i / tr.tau_d_I_i) ** (tr.tau_d_I_i / (tr.tau_r_I_i - tr.tau_d_I_i))
    namespace['invpeak_I_e'] = (tr.tau_r_I_e / tr.tau_d_I_e) ** (tr.tau_d_I_e / (tr.tau_r_I_e - tr.tau_d_I_e))

    g_exc = NeuronGroup(N=tr.N_e, model=neuron_model_exc,
                        threshold=tr.fr_threshold,
                        reset=tr.reset,
                        name='g_exc', namespace=namespace,
                        refractory=tr.t_ref_e,
                        method=tr.sim.integration_method)
    g_inh = NeuronGroup(N=tr.N_i, model=neuron_model_inh,
                        threshold=tr.netw.mod.fr_threshold,
                        reset=tr.reset,
                        name='g_inh', namespace=namespace,
                        refractory=tr.t_ref_i,
                        method=tr.sim.integration_method)

    # Synapses
    syn_ee = Synapses(target=g_exc, source=g_exc,
                      on_pre=tr.syn_EE_on_pre, delay=tr.syn_delay_ee,
                      namespace=namespace,
                      method=tr.sim.integration_method)
    syn_ei = Synapses(target=g_exc, source=g_inh,
                      on_pre=tr.syn_EI_on_pre, delay=tr.syn_delay_ei,
                      namespace=namespace,
                      method=tr.sim.integration_method)
    syn_ii = Synapses(target=g_inh, source=g_inh,
                      on_pre=tr.syn_II_on_pre, delay=tr.syn_delay_ii,
                      namespace=namespace,
                      method=tr.sim.integration_method)
    syn_ie = Synapses(target=g_inh, source=g_exc,
                      on_pre=tr.syn_IE_on_pre, delay=tr.syn_delay_ie,
                      namespace=namespace,
                      method=tr.sim.integration_method)

    # connect
    syn_ee.connect(p=tr.p_ee)
    syn_ii.connect(p=tr.p_ii)
    syn_ei.connect(p=tr.p_ei)
    syn_ie.connect(p=tr.p_ie)

    # init
    g_exc.V = np.random.normal(tr.E_E_rest / mV, 0.1, tr.N_e) * mV
    g_inh.V = np.random.normal(tr.E_I_rest / mV, 0.1, tr.N_i) * mV

    g_exc.Vt, g_inh.Vt = tr.Vt_e, tr.Vt_i
    g_exc.Vr, g_inh.Vr = tr.E_E_rest, tr.E_I_rest  # rest and reset values are the same here

    netw_objects.extend([g_exc, g_inh])
    netw_objects.extend([syn_ee, syn_ei, syn_ii, syn_ie])

    ############### SETUP MONITORS #####################
    record_spikes = True

    # record for LFP calculation (as sum of absolute values of currents on exc neurons)
    state_e = StateMonitor(g_exc, ('V', 'g_e', 'g_i'), record=True, dt=1*ms)  # TODO  dt is hardcoded
    # record for plots
    state_i = StateMonitor(g_inh, ('V', 'g_e', 'g_i'), record=True, dt=1*ms)  # TODO  dt is hardcoded

    lfp_e = PopulationRateMonitor(g_exc)  # instantaneous firing rates, averaged across neurons
    lfp_i = PopulationRateMonitor(g_inh)

    if record_spikes:
        m_e = SpikeMonitor(g_exc)
        m_i = SpikeMonitor(g_inh)

    netw_objects.append(state_e)
    netw_objects.extend([lfp_e, lfp_i])
    netw_objects.extend([m_e, m_i])

    ############### RUN #####################
    net = Network(*netw_objects)

    # duration = 0.5 * second
    duration = 0.1 * second

    net.run(duration, report='text', report_period=10 * second)

    ############### STORE RESULTS #####################

    print(tr.v_idx)
    run_dir = os.path.join(run_path, 'run_' + str(tr.v_idx))
    print(run_dir)
    os.mkdir(run_dir)

    save_conductance = False
    #### LFP based on currents sum ####
    # external drive
    cond_ = tr.netw.ext_drive * g_chr.values.T  # shape (12000, 10001)
    conductance_ext = cond_[:, :-1]  # (12000, 10000) TODO figure out the shape difference

    if save_conductance:
        np.save(run_dir + '\\voltage_e', state_e.V / mV)  # ndarray, shape (12000, 10000), so neurons x timepoints
        np.save(run_dir + '\\conductance_e', state_e.g_e / nS)  # ndarray, shape (12000, 10000), so neurons x timepoints
        np.save(run_dir + '\\conductance_i', state_e.g_i / nS)  # ndarray, shape (12000, 10000), so neurons x timepoints
        np.save(run_dir + '\\conductance_ext', conductance_ext)

    # calculate LFP

    def calculate_lfp(voltage_e, conductance_e, conductance_i, conductance_ext, E_e, E_i):
        '''
        Calculation of LFP as a sum of absolute values of all currents (exc and inh) on all excitatory cells.
        !leak currents are not included!
        Input and output unitless, values converted to base units (volts, siemens, ampers)
        '''
        # conductance_ext_ = conductance_ext[:, ::100]  # for ext_input with 0.01ms step
        conductance_ext_ = conductance_ext[:, ::10] # for ext_input with 0.1ms step
        if tr.netw.ext_drive > 0:  # TODO refactor later
            current_e = np.abs((conductance_e + conductance_ext_) * (E_e - voltage_e))
        else:
            current_e = np.abs((conductance_e) * (E_e - voltage_e))

        current_e_sum = np.sum(current_e, axis=0)

        current_i = np.abs(conductance_i * (E_i - voltage_e))
        current_i_sum = np.sum(current_i, axis=0)

        current_lfp = current_e_sum + current_i_sum

        return current_lfp

    lfp = calculate_lfp(state_e.V / volt, state_e.g_e / siemens, state_e.g_i / siemens, conductance_ext * 10 ** -9,
                        tr.E_E_e / volt, tr.E_E_i / volt)

    np.save(run_dir + '\\lfp', lfp)

    #### Populatin rate ####
    resolution_ = 0.5 * ms  # 0.2 is standard value
    population_rate_e = lfp_e.smooth_rate(window='gaussian', width=resolution_) / Hz
    population_rate_i = lfp_i.smooth_rate(window='gaussian', width=resolution_) / Hz

    np.save(run_dir + '\\population_rate_e', population_rate_e)
    np.save(run_dir + '\\population_rate_i', population_rate_i)

    #### Spiking #####
    # TODO spike_trains and spikes_/spike_times_ store the same type of information, store only one and convert
    # TODO it is now stored with units
    spike_trains_e = m_e.spike_trains()  # dict
    spike_trains_i = m_i.spike_trains()  # dict

    with open(run_dir + '\\spike_train_e', 'wb') as handle_e:
        pickle.dump(spike_trains_e, handle_e, protocol=pickle.HIGHEST_PROTOCOL)

    with open(run_dir + '\\spike_train_i', 'wb') as handle_i:
        pickle.dump(spike_trains_i, handle_i, protocol=pickle.HIGHEST_PROTOCOL)

    np.save(run_dir + '\\spikes_e', m_e.i)
    np.save(run_dir + '\\spikes_times_e', m_e.t / ms)

    np.save(run_dir + '\\spikes_i', m_i.i)
    np.save(run_dir + '\\spikes_times_i', m_i.t / ms)
