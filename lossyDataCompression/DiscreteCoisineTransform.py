import numpy as np
import time as time
import utils.DatasetOperations as ds_utils
import utils.DatasetsConstants as constants
import os
from scipy.fftpack import dct, idct

def dct2(block):
    return dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')


def idct2(coefficients):
    return idct(idct(coefficients, axis=0, norm='ortho'), axis=1, norm='ortho')


original_ds = os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH

ds = ds_utils.convertDateColumnToTimeseries(
    0, 1, ds_utils.readNumberArrayFromDataset(original_ds), format="%Y-%d")
block = np.array(ds)

start_time = time.time()
dct_block = dct2(block)
total_time = time.time() - start_time

print("Took: ", total_time)
print("In Memory Size saved:", ds_utils.commpareSizes(block, dct_block))
compressed_filename = "compressed_ds.csv"
ds_utils.saveDatasetInFile(compressed_filename, dct_block)

print("DS size difference is ", ds_utils.commpareSizes(original_ds, compressed_filename), " MB")

# print("\nReconstructed Block:")
# reconstructed_block = idct2(dct_block)
# print(reconstructed_block.round().astype(int))
