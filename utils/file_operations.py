import struct, os, pickle
from typing import List

def save_string_array_in_binary_file(encoded_data, file_path):
    with open(file_path, "wb") as file:
        for line in encoded_data:
            line_bytes = "".join(line).encode('utf-8')
            file.write(line_bytes)

def save_to_binary_file(encoded_data, file_path):
    with open(file_path, 'wb') as file:
        file.write(encoded_data.encode('utf-8'))
        
def save_list_to_binary_file(encoded_data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(encoded_data, file)
        
def save_num_array_to_binary_file(encoded_data: List[int], file_path):
    binary_data = struct.pack('i' * len(encoded_data), *encoded_data)

    with open(file_path, 'wb') as file:
        file.write(binary_data)

def read_integer_array_from_binary(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        num_elements = len(binary_data) // struct.calcsize('i')
        integer_array = struct.unpack('i' * num_elements, binary_data)
        
    return integer_array

def compare_file_sizes(original_file, encoded_file):
    original_file_size = os.path.getsize(original_file)
    encoded_file_size = os.path.getsize(encoded_file)
    
    return encoded_file_size/1000000, ((encoded_file_size * 100) / original_file_size)
