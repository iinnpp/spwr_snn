# membrane noise
from brian2 import mV
from pypet import cartesian_product

input_dict = {'ext_drive': [0.],
              'sigma_noise': [3.5, 4.0, 4.5, 5.0, 5.5]*mV}

# 'sigma_noise': [1., 1.5, 2., 2.5, 3.]*mV}  # no spikes

name = 'hdf5_data'
# explore_dict = n_list(input_dict) # check later if I need that
explore_dict = cartesian_product(input_dict)
