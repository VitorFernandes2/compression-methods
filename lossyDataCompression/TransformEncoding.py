import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import os
import utils.DatasetOperations as ds_utils
import utils.DatasetsConstants as constants

original_ds = os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH
ds = ds_utils.convertDateColumnToTimeseries(
    0, 1, ds_utils.readNumberArrayFromDataset(original_ds))
data = pd.DataFrame(ds)

pca = PCA(n_components=1)

# Fit PCA and transform the data
reduced_data = pca.fit_transform(data)

print("Original data:")
print(data)

print("\nEncoded data:")
print(reduced_data)
