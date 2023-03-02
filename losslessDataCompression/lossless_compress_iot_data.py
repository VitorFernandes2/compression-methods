import csv
from datetime import datetime
import logging
import os

# logging config
logging.basicConfig(level = logging.INFO)

# dataset location
AGRICULTURE_DATASET_PATH = "datasets/IOT-temp.csv"
SMOKE_DETECTION_DATASET_PATH = "datasets/smoke_detection_iot.csv"
ACCELEROMETER_DATASET_PATH = "datasets/accelerometer.csv"

# output file
ENCODED_DATASET_PATH = "encoded_dataset.csv"

# Create an array from a dataset
def createArrayFromDataset(datasetPath):
    with open(datasetPath, newline='') as csvfile:
        data = list(csvfile)
    data.pop(0)
    return data

def createArrayFromCsv(dataset_path):
    with open(dataset_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    data.pop(0)
    return data

# Convert a datetime to millis 
def convertDatetimeToMillis(time):
    return float(time * 1000)

# Apply both Delta Encoding algorithm and length encoding algorithm 
# to create a compressed dataset
def createEncodedDataset(dataset_path):
    dataset = createArrayFromCsv(dataset_path)

    # for each column in the dataset it will be substracted 
    # to the same in the previous row
    for row in reversed(range(len(dataset))):
        if row > 0:
            for column in reversed(range(len(dataset[0]))):
                    dataset[row][column] = round(float(dataset[row][column]) - float(dataset[row-1][column]), 3)
    
    rotated_dataset = list(zip(*dataset))[::-1]

    format_str = "{value}_{counter}"
    new_dataset = []
    for row in range(len(rotated_dataset)):
        counter = 0
        line = []
        for column in range(len(rotated_dataset[0])):
            if column > 0:
                if column < len(rotated_dataset[0]):
                    if rotated_dataset[row][column] == rotated_dataset[row][column-1]:
                        counter += 1
                    else:
                        entry = format_str.format(value= rotated_dataset[row][column], 
                                                  counter= counter)
                        line.append(entry) 
                        counter = 1
                else:
                    counter += 1
                    entry = format_str.format(value= rotated_dataset[row][column], 
                                              counter= counter)
                    line.append(entry) 
                    counter = 0
            else:
                counter += 1

        new_dataset.append(line)

    with open(ENCODED_DATASET_PATH, 'w') as testfile:
        for row in new_dataset:
            testfile.write(','.join([str(a) for a in row]) + '\n')
     
# In this function the aim is to measure the time that took to perform the dataset encoding 
# and the difference in size when compared to the original dataset
def main():
    start_date = datetime.now()
    ds_original_size = os.path.getsize(ACCELEROMETER_DATASET_PATH)
    
    logging.info("Started reading the iot data at %s, dataset orinal size=%i", start_date, ds_original_size)
     
    createEncodedDataset(ACCELEROMETER_DATASET_PATH)

    ds_final_size = os.path.getsize(ENCODED_DATASET_PATH)
    difference_percentage = 100 - round(float(ds_final_size * 100 / ds_original_size), 1)
    finish_date = datetime.now()
    total_time = convertDatetimeToMillis(finish_date.timestamp()) - convertDatetimeToMillis(start_date.timestamp())
    logging.info("Finished reading the iot data at %s and took %f millis and the reduction was %f %%", finish_date, total_time, difference_percentage)

# Call the main function to perform the measurements
main()
