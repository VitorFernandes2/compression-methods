import os
import time as time
import utils.file_operations as file_operations
import utils.datasets_constants as constants
import lossless_data_compression.bz2_encoding as encoder

file_paths = [
    os.getcwd() + constants.TIMESERIES_ACCELEROMETER,
    os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH,
    os.getcwd() + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_IOT_TEMP_PATH,
    os.getcwd() + constants.TIMESERIES_SMOKE_DETECTION_PATH,
]
OUTPUT_FILENAME = "compressed_ds.csv"

for original_filepath in file_paths:
    start_time = time.time()
    encoder.compress_file(original_filepath, OUTPUT_FILENAME)
    total_time = time.time() - start_time

    size_diff, percentage_diff = file_operations.compare_file_sizes(
        original_filepath, OUTPUT_FILENAME)
    
    print("Dataset:", original_filepath.replace(os.getcwd(), ''))
    print("Took: ", total_time)
    print("Size difference:", size_diff, "MB")
    print("Percentage difference:", 100 - percentage_diff, "%\n ")
