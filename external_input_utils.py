import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def gaussian_form(t, sigma, mu):
    return (1. / (np.sqrt(2. * np.pi * sigma ** 2))) * np.exp(-(t - mu) ** 2 / (2.0 * sigma ** 2))


def generate_ext_input(duration, N_e, n_excited, exc_drive_amplitude, dt, verbose=False, active_cells=None):
    """
    Excitation shifted in time.
    TEMPORAL JITTER IS HARDCODED!

    duration: in ms
    n_excited: number of units receiving excitation
    N_e: total number of units
    exc_drive_amplitude: mimics SPW amplitude (max amplitude)
    dt: time step

    out:
    list with input values (len = number of timepoints, each element is 1d 12000(N_e) element array)
    array with idx of excited cells
    """
    # time_step_array = 0.01 #ms
    time_a = np.arange(0.0, duration + dt, dt)
    if verbose:
        print('duration {} ms, time step {}, array shape {}'.format(duration, dt, time_a.shape))
        print('time start {} ms, end {} ms'.format(time_a[0], time_a[-1]))

    # choose a subset of excitatory cells randomly
    if active_cells is None:
        E_cells = np.arange(N_e)
        shuffled_E_cells = np.random.permutation(E_cells)
        shuffled_E_cells = shuffled_E_cells[0:n_excited]
    else:
        shuffled_E_cells = active_cells
    active_neurons = np.zeros(N_e)
    active_neurons[shuffled_E_cells] = 1.0

    ##### MAKING AMPLITUDE #####
    # amplitude is the same for all excited neurons
    mean_intensity = exc_drive_amplitude
    amplitude = mean_intensity * np.ones(N_e)
    amplitude *= active_neurons  # array with non-zero amplitude for excited E cells

    ##### MAKING TIME #####
    peak_time_zero_mean = 50.0
    peak_time_zero = np.random.normal(peak_time_zero_mean, 10.0, N_e)  # temporal variation around

    temporal_sigma = 3.0
    normalization = 1. / np.sqrt(2. * np.pi * temporal_sigma ** (2))

    array_gaussian = []
    for j in np.arange(0, len(time_a)):
        random_activation = np.zeros(len(amplitude))
        random_activation = (amplitude) * (1. / normalization) * (
            gaussian_form(time_a[j], temporal_sigma, peak_time_zero))
        array_gaussian.append(random_activation)

    result = {'excited_cells': shuffled_E_cells,
              'waveforms': array_gaussian,
              'dt': dt,
              'duration': duration}

    return result


def generate_empty_input(duration, dt, N_e):
    """
    TODO refactor
    generates list with 0
    :param duration:
    :param N_e:
    :return:
    """
    empty_input = []

    length = int(duration/dt + 1)
    for i in range(length):
        empty_input.append(np.zeros(N_e))

    return empty_input


def generate_multiple_spw(duration, n_spw, N_e, n_excited, exc_drive_amplitude, dt, verbose=False):
    """
    TODO refactor
    n_spw: number of periods with drive

    Generate external input with n_spw "spw".
    1. Make list (len=duration, each element is 1xN_e array), fill with zeros
    2. Call generate_ext_input n_spw time
    3. Put generated spw in the list.

    :return:
    """
    spw_duration = 100  # ms
    spw_dt = dt

    full_input = []

    empty_input = generate_empty_input(spw_duration, spw_dt, N_e)

    spw = generate_ext_input(spw_duration, N_e, n_excited, exc_drive_amplitude, spw_dt, verbose=False)

    full_input += empty_input
    full_input += spw['waveforms'][1:]
    full_input += empty_input[1:]

    excited_cells = spw['excited_cells']

    for i in range(1, n_spw):
        spw = generate_ext_input(spw_duration, N_e, n_excited, exc_drive_amplitude, spw_dt, False, excited_cells)
        full_input += spw['waveforms'][1:]
        full_input += empty_input[1:]

    result = {'excited_cells': excited_cells,
              'waveforms': full_input,
              'dt': dt,
              'duration': duration}

    return result


def plot_ext_input(ext_input_dict, file_name=None, save_fig=False):
    ext_input_a = np.asarray(ext_input_dict['waveforms'])
    time_a = np.arange(0.0, ext_input_dict['duration'] + ext_input_dict['dt'], ext_input_dict['dt'])

    fontsize_ = 18
    fig, axes = plt.subplots(figsize=(10, 5))

    for i, j in enumerate(ext_input_dict['excited_cells']):
        axes.plot(time_a, ext_input_a[:, j], color='black', alpha=0.5, linewidth=0.5)

        #axes.axvline(x=50, color='red', linewidth=1)

    axes.set_xlabel('Time (ms)', fontsize=fontsize_)
    axes.set_ylabel('Amplitude (nS)', fontsize=fontsize_)

    axes.set_ylim(0, 100)
    axes.tick_params(labelsize=fontsize_)

    sns.despine()

    if save_fig:
        # TODO fix path
        # fig.savefig(file_name)
        plt.savefig('D:\\poster_illustrator\\figures\\r_fig_6\\external_input.svg', bbox_inches='tight')
