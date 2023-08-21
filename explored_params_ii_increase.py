# II inhibition increase
from brian2 import mV, ms
from pypet import cartesian_product

input_dict = {'c_gii': [0.05, 0.06, 0.07, 0.08, 0.09, 0.095, 0.0955, 0.096, 0.0965, 0.097, 0.0975, 0.098, 0.0985, 0.099, 0.0995, 0.1, 0.2, 0.3, 0.4,
                        0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.],
              'ext_drive': [1.],
              'sigma_noise': [5.0] * mV,
              'dt': [0.1] * ms
              }

name = 'hdf5_data'
explore_dict = cartesian_product(input_dict)
