from datetime import datetime
import logging
import os
from LZ77 import LZ77Compressor

# logging config
logging.basicConfig(level = logging.INFO)

# dataset location
DAILY_MINIMUM_TEMPERATURE_DATASET_PATH = "../../datasets/timeseries/daily-minimum-temperatures-in-me.csv"

# output file
ENCODED_DATASET_PATH = "../../encoded_dataset.csv"

# Convert a datetime to millis 
def convertDatetimeToMillis(time):
    return float(time * 1000)

start_date = datetime.now()
ds_original_size = os.path.getsize(DAILY_MINIMUM_TEMPERATURE_DATASET_PATH)

LZ77Compressor(400).compress(DAILY_MINIMUM_TEMPERATURE_DATASET_PATH, ENCODED_DATASET_PATH)

ds_final_size = os.path.getsize(ENCODED_DATASET_PATH)
difference_percentage = 100 - round(float(ds_final_size * 100 / ds_original_size), 1)
finish_date = datetime.now()
total_time = convertDatetimeToMillis(finish_date.timestamp()) - convertDatetimeToMillis(start_date.timestamp())
logging.info("Finished reading the iot data at %s and took %f millis and the reduction was %f %%", finish_date, total_time, difference_percentage)

