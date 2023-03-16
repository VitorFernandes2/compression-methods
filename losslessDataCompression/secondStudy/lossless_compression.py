from datetime import datetime
import logging
import os
from LZ77 import LZ77Compressor
from LZ78 import LZ78Compressor

# logging config
logging.basicConfig(level = logging.INFO)

# dataset location
DAILY_MINIMUM_TEMPERATURE_DATASET_PATH = "../../datasets/timeseries/daily-minimum-temperatures-in-me.csv"
ELETRIC_PRODUCTION_DATASET_PATH = "../../datasets/timeseries/Electric_Production.csv"
MONTHLY_BEER_PRODUCTION_DATASET_PATH = "../../datasets/timeseries/monthly-beer-production-in-austr.csv"
SALES_OF_SHAMPOO_DATASET_PATH = "../../datasets/timeseries/sales-of-shampoo-over-a-three-ye.csv"

# output file
ENCODED_DATASET_PATH = "../../encoded_dataset.csv"

#Window Size
WINDOW_SIZE = 400

# Convert a datetime to millis 
def convertDatetimeToMillis(time):
    return float(time * 1000)

ORIGINAL_DATASET = DAILY_MINIMUM_TEMPERATURE_DATASET_PATH

start_date = datetime.now()
ds_original_size = os.path.getsize(ORIGINAL_DATASET)

# LZ77Compressor(WINDOW_SIZE).compress(ORIGINAL_DATASET, ENCODED_DATASET_PATH)
LZ78Compressor().compress(ORIGINAL_DATASET, ENCODED_DATASET_PATH)

ds_final_size = os.path.getsize(ENCODED_DATASET_PATH)
difference_percentage = 100 - round(float(ds_final_size * 100 / ds_original_size), 1)
finish_date = datetime.now()
total_time = convertDatetimeToMillis(finish_date.timestamp()) - convertDatetimeToMillis(start_date.timestamp())
logging.info("Finished reading the iot data at %s and took %f millis and the reduction was %f %%", finish_date, total_time, difference_percentage)

