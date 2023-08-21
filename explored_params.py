# membrane noise
from brian2 import mV, ms
from pypet import cartesian_product

input_dict = {'ext_drive': [1.],
              'sigma_noise': [5.0]*mV,
              'dt': [0.1]*ms}

name = 'hdf5_data'
# explore_dict = n_list(input_dict) # check later if I need that
explore_dict = cartesian_product(input_dict)
