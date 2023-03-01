from datetime import datetime
import logging
import os
from conversion_utils import DecodeIntegerToString, EncodeStringToInteger
from length_encoding import LengthEncoding

# logging config
logging.basicConfig(level = logging.INFO)

# dataset location
AGRICULTURE_DATASET_PATH = "datasets/IOT-temp.csv"
SMOKE_DETECTION_DATASET_PATH = "datasets/smoke_detection_iot.csv"

# convert a datetime to millis 
def convertDatetimeToMillis(time):
    return float(time * 1000)

# In this function the aim is to measure the time that took to perform the dataset encoding 
# and the difference in size when compared to the original dataset
def main():
    start_date = datetime.now()
    agriculture_ds_original_size = os.path.getsize(AGRICULTURE_DATASET_PATH)
    smoke_detection_ds_original_size = os.path.getsize(AGRICULTURE_DATASET_PATH)
    
    logging.info("Started reading the iot data at %s, agriculture ds orinal size=%i, smoke detection dataset original size=%i", start_date, agriculture_ds_original_size, smoke_detection_ds_original_size)
    
    encodedValue = LengthEncoding("Hello world!")
    print(encodedValue)

    finish_date = datetime.now()
    total_time = convertDatetimeToMillis(finish_date.timestamp()) - convertDatetimeToMillis(start_date.timestamp())
    
    logging.info("Finished reading the iot data at %s and took %f millis", finish_date, total_time)

# call the main function to perform the measurements
main()
