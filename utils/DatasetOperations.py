import pandas as pd
from datetime import datetime
import time
import sys
import csv
import os

"""
Read the path of the dataset and return a 2D array of the numeric values
:param path: The path to the dataset
:return: 2D array of values from dataset 
"""
def readNumberArrayFromDataset(path):
    ds = pd.read_csv(path)
    return ds.values

def convertDateColumnToTimeseries(date_column, data_column, dataset):
    return [[int(time.mktime(datetime.strptime(row[date_column], "%m/%d/%Y").timetuple())), int(row[data_column] * 100)] for row in dataset]

def commpareSizes(original_ds, compressed_ds):
    size = sys.getsizeof(original_ds) - sys.getsizeof(compressed_ds)
    return  size / 1024

def saveDatasetInFile(file_path, ds):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in ds:
            writer.writerow(row)

def getFileSizeKB(file_path):
    return os.path.getsize(file_path) /1024
            
def getFileSizeMB(file_path):
    return getFileSizeKB(file_path) / 1024