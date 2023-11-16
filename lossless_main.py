import utils.datasets_constants as constants
from lossless_data_compression import delta_encoding_string
import os
import utils.file_operations as file_operations
import time

file_path = os.getcwd() + constants.TIMESERIES_SMOKE_DETECTION_PATH

with open(file_path, 'r') as file:
    file_content_lines = file.readlines()
    
data = file_content_lines
# Array without the header
valid_data = ''.join(data[1:])

start_time = time.time()
encoded_data = delta_encoding_string.delta_encode_string(valid_data)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000

output_path = os.getcwd() + "/output/output.bin"
file_operations.save_to_binary_file(''.join(encoded_data), output_path)

#print("Decoded data: ", delta_encoding_string.delta_decode_string(file_operations.read_integer_array_from_binary(output_path)))

size_diff, percentage_diff = file_operations.compare_file_sizes(file_path, output_path)
print("The algorythms took", elapsed_time, "to obtain", size_diff, "corresponding to ", percentage_diff, "%")