import os
import time as time
import utils.datasets_constants as constants
import utils.file_operations as file_operations
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")

def find_optimal_k(data, max_k=10):
    distortions = []

    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        distortions.append(kmeans.inertia_)  # Inertia is the sum of squared distances to the closest centroid

    # Choose the "elbow" point as the optimal k
    optimal_k = elbow_point(distortions)
    return optimal_k

def elbow_point(distortions):
    # Find the "elbow" point in the graph
    # This is a simplistic approach; you may need more sophisticated methods
    # such as the second derivative test or statistical methods for a more robust solution
    deltas = [distortions[i] - distortions[i + 1] for i in range(len(distortions) - 1)]
    optimal_k_index = deltas.index(max(deltas)) + 1
    return optimal_k_index + 1  # Add 1 to get the optimal k value

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


scaler = StandardScaler()

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

    scaled_data = scaler.fit_transform(df)
    
    optimal_k = find_optimal_k(scaled_data)
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_data)
    compressed_data = kmeans.cluster_centers_[cluster_labels]
    
    # End Compression
    total_time = time.time() - start_time

    # Reconstruct the original data using cluster centers and assignments
    reconstructed_data = kmeans.cluster_centers_[cluster_labels]

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

    # Evaluate compression performance (for example, mean squared error)
    mse = np.mean((scaled_data - reconstructed_data) ** 2)
    print(f"Mean Squared Error: {mse}")
    
    print("K: ", optimal_k)
    print("Took: ", total_time)
    print("Size difference:", size_diff, "MB")
    print("Percentage difference:", 100-percentage_diff, "%\n")
