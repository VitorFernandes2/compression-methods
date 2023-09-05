import numpy as np
import pywt
import os
import utils.DatasetOperations as ds_utils
import utils.DatasetsConstants as constants

def wavelet_compression(data, wavelet='haar', level=1, threshold=0.1):
    # Perform 1D wavelet transform
    coeffs = pywt.wavedec(data, wavelet, level=level)

    # Apply thresholding to coefficients
    def threshold_function(coef):
        return pywt.threshold(coef, value=threshold*max(coef))

    thresholded_coeffs = [threshold_function(coef) for coef in coeffs]

    # Reconstruct the compressed data
    compressed_data = pywt.waverec(thresholded_coeffs, wavelet)

    return compressed_data

original_ds = os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH
ds = ds_utils.convertDateColumnToTimeseries(
    0, 1, ds_utils.readNumberArrayFromDataset(original_ds))

original_data = np.array(ds)
compressed_data = wavelet_compression(original_data, wavelet='haar', level=1, threshold=0.1)

print("Original Data:", original_data)
print("Compressed Data:", compressed_data)
