from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import os
import utils.datasets_constants as constants
import utils.file_operations as file_operations

file_paths = [
    os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH,
    os.getcwd() + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_ACCELEROMETER,
    os.getcwd() + constants.TIMESERIES_SMOKE_DETECTION_PATH,
    os.getcwd() + constants.TIMESERIES_IOT_TEMP_PATH,
]

vectorizer = TfidfVectorizer()

# Start time of compression
n_components = 2  
pca = PCA(n_components=n_components)

for file_path in file_paths:
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    start_time = time.time()
    
    encoded_data = []
    for i, line in enumerate(data):
        encoded_data.append(line)

    tfidf_matrix = vectorizer.fit_transform(encoded_data).toarray()
    compressed_data = pca.fit_transform(tfidf_matrix)
    
    # End time of compression
    end_time = time.time()
    
    reconstructed_data = pca.inverse_transform(compressed_data)

    elapsed_time = (end_time - start_time) * 1000

    output_path = os.getcwd() + "/output/output.bin"
    file_operations.save_list_to_binary_file(encoded_data, output_path)

    size_diff, percentage_diff = file_operations.compare_file_sizes(
        file_path, output_path)
    print(file_path, "The algorythms took", elapsed_time, "to obtain",
          size_diff, "corresponding to ", (100 - percentage_diff), "%")
