import os
import time as time
import utils.datasets_constants as constants
import utils.file_operations as file_operations
import pandas as pd
import numpy as np

base_path = os.getcwd()

file_paths = [
    base_path + constants.TIMESERIES_ACCELEROMETER,
    base_path + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH,
    base_path + constants.TIMESERIES_DAILY_MINIMUM_PATH,
    base_path + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH,
    base_path + constants.TIMESERIES_IOT_TEMP_PATH,
    base_path + constants.TIMESERIES_SMOKE_DETECTION_PATH,
]
OUTPUT_FILENAME = "compressed_ds.csv"
ds_main_field_dict = {
    base_path + constants.TIMESERIES_ACCELEROMETER: "x",
    base_path + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH: "Monthly beer production",
    base_path + constants.TIMESERIES_DAILY_MINIMUM_PATH: "Daily minimum temperatures",
    base_path + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH: "IPG2211A2N",
    base_path + constants.TIMESERIES_IOT_TEMP_PATH: "temp",
    base_path + constants.TIMESERIES_SMOKE_DETECTION_PATH: "eCO2[ppm]",
}

for file_path in file_paths:
    original_df = pd.DataFrame(pd.read_csv(file_path))
    df = original_df.copy() # Clone the original dataframe

    print("Dataset:", file_path.replace(base_path, ''))

    # Apply random projection for compression
    main_column = ds_main_field_dict.get(file_path)
        
    # Start compression
    start_time = time.time()

    subsampled_data = df.sample(n=df.shape[0], weights=df.groupby(main_column)[main_column].transform('count'))

    # End Compression
    total_time = time.time() - start_time

    subsampled_data.to_csv(OUTPUT_FILENAME, sep=',', index=False, encoding='utf-8')
    size_diff, percentage_diff = file_operations.compare_file_sizes(
    file_path, OUTPUT_FILENAME)

    print("Took: ", total_time)
    print("Size difference:", size_diff, "MB")
    print("Percentage difference:", 100-percentage_diff, "%\n")
