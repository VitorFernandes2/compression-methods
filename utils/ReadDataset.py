import pandas as pd

"""
Read the path of the dataset and return a 2D array of the numeric values
:param path: The path to the dataset
:return: 2D array of values from dataset 
"""
def readNumberArrayFromDataset(path):
    ds = pd.read_csv(path)
    return ds.values
