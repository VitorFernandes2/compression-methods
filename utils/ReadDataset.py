import pandas as pd
from datetime import datetime
import time

"""
Read the path of the dataset and return a 2D array of the numeric values
:param path: The path to the dataset
:return: 2D array of values from dataset 
"""
def readNumberArrayFromDataset(path):
    ds = pd.read_csv(path)
    return ds.values

def convertDateColumnToTimeseries(date_column, data_column, dataset):
    return [[int(time.mktime(datetime.strptime(row[date_column], "%m/%d/%Y").timetuple())), float(row[data_column])] for row in dataset]
