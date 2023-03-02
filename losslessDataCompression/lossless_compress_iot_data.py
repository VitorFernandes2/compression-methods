from datetime import datetime
import logging
import os
from conversion_utils import EncodeStringToInteger
from length_encoding import LengthEncoding
from elias_delta_encode import EliasDeltaEncode

# logging config
logging.basicConfig(level = logging.INFO)

# dataset location
AGRICULTURE_DATASET_PATH = "datasets/IOT-temp.csv"
SMOKE_DETECTION_DATASET_PATH = "datasets/smoke_detection_iot.csv"
ENCODED_DATASET_PATH = "encoded_dataset.csv"

# Create an array from a dataset
def createArrayFromDataset(datasetPath):
    with open(datasetPath, newline='') as csvfile:
        data = list(csvfile)
    data.pop(0)
    return data

# Convert a datetime to millis 
def convertDatetimeToMillis(time):
    return float(time * 1000)

# Apply both Delta Encoding algorithm and length encoding algorithm 
# to create a compressed dataset
def createEncodedDataset(dataset_path):
    # TODO: For each line of the csv 
    #           * Convert it to integer
    #           * Apply Delta Encoding
    #           * Apply Length Encoding
    #       Create the new dataset with encoded values

    encode_string_to_int = EncodeStringToInteger("...")
    delta_encoding = EliasDeltaEncode(encode_string_to_int)
    LengthEncoding(delta_encoding)

# In this function the aim is to measure the time that took to perform the dataset encoding 
# and the difference in size when compared to the original dataset
def main():
    start_date = datetime.now()
    ds_original_size = os.path.getsize(AGRICULTURE_DATASET_PATH)
    
    logging.info("Started reading the iot data at %s, dataset orinal size=%i", start_date, ds_original_size)
     
    createEncodedDataset(AGRICULTURE_DATASET_PATH)

    finish_date = datetime.now()
    total_time = convertDatetimeToMillis(finish_date.timestamp()) - convertDatetimeToMillis(start_date.timestamp())
    logging.info("Finished reading the iot data at %s and took %f millis", finish_date, total_time)

# Call the main function to perform the measurements
main()
