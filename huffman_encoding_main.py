import lossless_data_compression.huffman_encoding as huffman_encoding
import time
import os
import utils.datasets_constants as constants
import utils.file_operations as file_operations

file_paths = [
    os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH,
    os.getcwd() + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_ACCELEROMETER,
    os.getcwd() + constants.TIMESERIES_IOT_TEMP_PATH,
    os.getcwd() + constants.TIMESERIES_SMOKE_DETECTION_PATH,
]

for file_path in file_paths:
    with open(file_path, 'r') as file:
        data = file.readlines()

    start_time = time.time()

    frequencies = huffman_encoding.Counter(data)
    tree = huffman_encoding.build_tree(frequencies)
    codes = huffman_encoding.generate_codes(tree)
    encoded_data = huffman_encoding.encode(data, codes)

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000

    tree_output_path = os.getcwd() + "/output/tree.bin"
    file_operations.save_list_to_binary_file(frequencies, tree_output_path)

    output_path = os.getcwd() + "/output/output.bin"
    file_operations.save_list_to_binary_file(encoded_data, output_path)
    
    original_file_size = os.path.getsize(file_path)
    print("##############################################")
    print("Without tree")
    
    encoded_file_size = os.path.getsize(output_path)
    size_diff = encoded_file_size / 1000000
    percentage_diff = ((encoded_file_size * 100) / original_file_size)
    print(file_path, "The algorythms took", elapsed_time, "to obtain",
          size_diff, "corresponding to ", (100 - percentage_diff), "%")
    
    print("##############################################")
    print("With tree")
    
    encoded_file_size = os.path.getsize(tree_output_path) + os.path.getsize(output_path)
    size_diff = encoded_file_size / 1000000
    percentage_diff = ((encoded_file_size * 100) / original_file_size)
    print(file_path, "The algorythms took", elapsed_time, "to obtain",
          size_diff, "corresponding to ", (100 - percentage_diff), "%")
    print("\n\n")
