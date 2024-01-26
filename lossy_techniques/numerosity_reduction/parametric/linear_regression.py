import os
import time as time
import utils.datasets_constants as constants
import utils.file_operations as file_operations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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
timeseries_columns = ["Month", "Date", "DATE", "noted_date"]
columns_to_drop = ["id","room_id/id","out/in"]

# Fit a linear regression model
model = LinearRegression()
    
for file_path in file_paths:
    original_df = pd.DataFrame(pd.read_csv(file_path))
    df = original_df.copy() # Clone the original dataframe
    matching_columns = [column for column in df.columns if column in timeseries_columns]

    print("Dataset:", file_path.replace(base_path, ''))
    if matching_columns:
        # Remove string columns
        df = df.drop(columns=columns_to_drop, axis=1, errors="ignore")
        for col in matching_columns:
            df[col] = pd.to_datetime(df[col], format="mixed")
            min_datetime = df[col].min()
            df[col] = (df[col] - min_datetime).dt.total_seconds()

    # Start compression
    start_time = time.time()

    # Split the data into training and testing sets
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
    # Fit a linear regression model
    model.fit(X_train, X_train)
    
    # Use the model to reconstruct the dataset
    compressed_data = model.predict(X_test)
    
    # End Compression
    total_time = time.time() - start_time

    # Display the compressed dataset
    compressed_df = pd.DataFrame(data=compressed_data)
    
    # Reduce the decimal cases to two decimal cases 
    for column in compressed_df.select_dtypes(include='number').columns:
        compressed_df[column] = compressed_df[column].round(decimals=2)
    
    # Concatenate the droped fields if exists
    for column_name in columns_to_drop:
        if column_name in original_df.columns:
            compressed_df.insert(loc=len(compressed_df.columns), column=column_name, value=original_df[column_name])
    
    compressed_df.to_csv(OUTPUT_FILENAME, sep=',', index=False, encoding='utf-8')
    size_diff, percentage_diff = file_operations.compare_file_sizes(
    file_path, OUTPUT_FILENAME)

    print("Took: ", total_time)
    print("Size difference:", size_diff, "MB")
    print("Percentage difference:", 100-percentage_diff, "%\n")
