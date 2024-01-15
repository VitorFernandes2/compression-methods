import os
import time as time
import utils.datasets_constants as constants
import utils.file_operations as file_operations
import pandas as pd

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
float_cols_dictionary = {
    base_path + constants.TIMESERIES_ACCELEROMETER: ["x", "y", "z"],
    base_path + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH: ["IPG2211A2N"],
    base_path + constants.TIMESERIES_SMOKE_DETECTION_PATH: ["Temperature[C]", "Pressure[hPa]"],
}

DECIMAL_CASES = 2

for file_path in file_paths:
    col_array = float_cols_dictionary.get(file_path)
    if col_array is not None:
        df = pd.DataFrame(pd.read_csv(file_path))

        print("Dataset:", file_path.replace(base_path, ''))

        # Start compression
        start_time = time.time()

        for col in col_array:
            df[col] = df[col].apply(lambda x: round(x, DECIMAL_CASES))

        # End Compression
        total_time = time.time() - start_time

        df.to_csv(OUTPUT_FILENAME, sep=',', index=False, encoding='utf-8')
        size_diff, percentage_diff = file_operations.compare_file_sizes(
            file_path, OUTPUT_FILENAME)

        print("Took: ", total_time)
        print("Size difference:", size_diff, "MB")
        print("Percentage difference:", 100-percentage_diff, "%\n")
