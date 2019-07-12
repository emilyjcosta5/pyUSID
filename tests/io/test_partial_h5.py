"""
This script creates a partial h5py file then tests the process class with it.
Created on: Jul 12, 2019
Author: Emily Costa
"""

from data_utils import make_sparse_sampling_file
import pyUSID as usid
from pyUSID.io import dtype_utils, hdf_utils
import h5py
import os


# Creates incomplete h5py dataset object in current path
h5_path = 'sparse_sampling.h5'
if not os.path.exists(h5_path):
    make_sparse_sampling_file()
h5_f = h5py.File(h5_path, mode='r+')
hdf_utils.print_tree(h5_f)
h5_main0 = h5_f['Measurement_000/Channel_000/Raw_Data']
h5_main1 = h5_f['Measurement_000/Channel_001/Raw_Data']

print(hdf_utils.simple.check_if_main(h5_main0, verbose=True))
#dtype_utils.check_dtype(h5_main)

