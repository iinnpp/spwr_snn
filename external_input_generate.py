# first 2 lines to run in the console
import os
sys.path.append(os.path.join(os.getcwd(), 'brian_models/ripples_2populations_v2'))

from external_input_utils import generate_ext_input, plot_ext_input, generate_multiple_spw
import pickle

### Generate 100ms input with dt=0.1
duration = 100
N_e = 12000
n_excited = 1580
exc_drive_amplitude=83.0
dt = 0.1

ext_input_100ms_dt0_1 = generate_ext_input(duration, N_e, n_excited, exc_drive_amplitude, dt, verbose=False)

data_path = 'D:\\00_modeling\\model_results\\tests\\'
with open(data_path + '\\ext_input_100ms_dt0_1', 'wb') as handle:
    pickle.dump(ext_input_100ms_dt0_1, handle, protocol=pickle.HIGHEST_PROTOCOL)

### Generate new input

duration = 500
N_e = 12000
n_excited = 1580
exc_drive_amplitude=83.0
dt = 0.1

n_spw = 2

ext_input_mult_dict = generate_multiple_spw(duration, n_spw, N_e, n_excited, exc_drive_amplitude, dt, verbose=False)

data_path = 'D:\\00_modeling\\model_results\\tests\\'
with open(data_path + '\\ext_input_mult_dict_500ms_2spw', 'wb') as handle:
    pickle.dump(ext_input_mult_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# if generate_ext_input:
#     ext_input_dict = generate_ext_input(duration, N_e, n_excited, exc_drive_amplitude, dt)
#     if save_ext_input:
#         with open(data_path + '\\ext_input_dict_1', 'wb') as handle:
#             pickle.dump(ext_input_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
# else:
#     with open(data_path + '\\ext_input_dict_1', 'rb') as handle:
#         ext_input_dict = pickle.load(handle)


# ext_input_dict = generate_ext_input(duration, N_e, n_excited, exc_drive_amplitude, dt) # 100ms with 1 spw


### Plot (and load)
with open(data_path + '\\ext_input_mult_dict_500ms_2spw', 'rb') as handle:
    ext_input_mult_dict = pickle.load(handle)

plot_ext_input(ext_input_mult_dict, None, save_fig=False)


