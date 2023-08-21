from pypet.brian2.parameter import Brian2Parameter
import standard_params as prm
import models as mod


def add_params(tr):
    tr.v_standard_parameter = Brian2Parameter
    tr.v_fast_access = True

    tr.f_add_parameter('netw.N_e', prm.N_e)
    tr.f_add_parameter('netw.N_i', prm.N_i)

    tr.f_add_parameter('netw.p_ee', prm.p_ee)
    tr.f_add_parameter('netw.p_ie', prm.p_ie)
    tr.f_add_parameter('netw.p_ei', prm.p_ei)
    tr.f_add_parameter('netw.p_ii', prm.p_ii)

    tr.f_add_parameter('netw.E_E_e', prm.E_E_e)
    tr.f_add_parameter('netw.E_E_i', prm.E_E_i)
    tr.f_add_parameter('netw.E_E_rest', prm.E_E_rest)
    tr.f_add_parameter('netw.C_e', prm.C_e)
    tr.f_add_parameter('netw.gl_e', prm.gl_e)
    tr.f_add_parameter('netw.Vt_e', prm.Vt_e)
    tr.f_add_parameter('netw.t_ref_e', prm.t_ref_e)

    tr.f_add_parameter('netw.E_I_e', prm.E_I_e)
    tr.f_add_parameter('netw.E_I_i', prm.E_I_i)
    tr.f_add_parameter('netw.E_I_rest', prm.E_I_rest)
    tr.f_add_parameter('netw.C_i', prm.C_i)
    tr.f_add_parameter('netw.gl_i', prm.gl_i)
    tr.f_add_parameter('netw.Vt_i', prm.Vt_i)
    tr.f_add_parameter('netw.t_ref_i', prm.t_ref_i)

    tr.f_add_parameter('netw.config.syn_cond_mode_ee', prm.syn_cond_mode_ee)
    tr.f_add_parameter('netw.config.syn_cond_mode_ei', prm.syn_cond_mode_ei)
    tr.f_add_parameter('netw.config.syn_cond_mode_ii', prm.syn_cond_mode_ii)
    tr.f_add_parameter('netw.config.syn_cond_mode_ie', prm.syn_cond_mode_ie)

    tr.f_add_parameter('netw.tau_r_E_e', prm.tau_r_E_e)
    tr.f_add_parameter('netw.tau_d_E_e', prm.tau_d_E_e)
    tr.f_add_parameter('netw.g_peak_E_e', prm.g_peak_E_e)

    tr.f_add_parameter('netw.tau_r_E_i', prm.tau_r_E_i)
    tr.f_add_parameter('netw.tau_d_E_i', prm.tau_d_E_i)
    tr.f_add_parameter('netw.g_peak_E_i', prm.g_peak_E_i)

    tr.f_add_parameter('netw.tau_r_I_e', prm.tau_r_I_e)
    tr.f_add_parameter('netw.tau_d_I_e', prm.tau_d_I_e)
    tr.f_add_parameter('netw.g_peak_I_e', prm.g_peak_I_e)

    tr.f_add_parameter('netw.tau_r_I_i', prm.tau_r_I_i)
    tr.f_add_parameter('netw.tau_d_I_i', prm.tau_d_I_i)
    tr.f_add_parameter('netw.g_peak_I_i', prm.g_peak_I_i)

    tr.f_add_parameter('netw.syn_delay_ee', prm.syn_delay_ee)
    tr.f_add_parameter('netw.syn_delay_ei', prm.syn_delay_ei)
    tr.f_add_parameter('netw.syn_delay_ii', prm.syn_delay_ii)
    tr.f_add_parameter('netw.syn_delay_ie', prm.syn_delay_ie)

    tr.f_add_parameter('netw.sigma_noise', prm.sigma_noise)

    tr.f_add_parameter('netw.ext_drive', prm.ext_drive)

    tr.f_add_parameter('netw.sim.dt', prm.dt)
    tr.f_add_parameter('netw.sim.integration_method', prm.integration_method)

    tr.f_add_parameter('netw.c_ge', prm.c_ge)
    tr.f_add_parameter('netw.c_gi', prm.c_gi)

    tr.f_add_parameter('netw.c_gee', prm.c_gee)
    tr.f_add_parameter('netw.c_gei', prm.c_gei)
    tr.f_add_parameter('netw.c_gii', prm.c_gii)
    tr.f_add_parameter('netw.c_gie', prm.c_gie)

    tr.f_add_parameter('netw.mod.lif_exc', mod.lif_exc)
    tr.f_add_parameter('netw.mod.lif_inh', mod.lif_inh)

    tr.f_add_parameter('netw.mod.syn_EE_biexp', mod.syn_EE_biexp)
    tr.f_add_parameter('netw.mod.syn_IE_biexp', mod.syn_IE_biexp)
    tr.f_add_parameter('netw.mod.syn_II_biexp', mod.syn_II_biexp)
    tr.f_add_parameter('netw.mod.syn_EI_biexp', mod.syn_EI_biexp)

    tr.f_add_parameter('netw.mod.fr_threshold', mod.fr_threshold)
    tr.f_add_parameter('netw.mod.reset', mod.reset)

    tr.f_add_parameter('netw.mod.syn_EE_on_pre', mod.syn_EE_on_pre)
    tr.f_add_parameter('netw.mod.syn_EI_on_pre', mod.syn_EI_on_pre)
    tr.f_add_parameter('netw.mod.syn_II_on_pre', mod.syn_II_on_pre)
    tr.f_add_parameter('netw.mod.syn_IE_on_pre', mod.syn_IE_on_pre)



