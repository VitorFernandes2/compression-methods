import utils.datasets_constants as constants
import time
import os

file_paths = [
    os.getcwd() + constants.TIMESERIES_ACCELEROMETER,
    os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_DAILY_MINIMUM_PATH,
    os.getcwd() + constants.TIMESERIES_ELETRIC_PRODUCTION_PATH,
    os.getcwd() + constants.TIMESERIES_IOT_TEMP_PATH,
    os.getcwd() + constants.TIMESERIES_SMOKE_DETECTION_PATH,
]

def burrows_wheeler_transform(input_string):
    # Add a unique sentinel character not present in the input
    input_string += '\0'

    # Create a list of all cyclic rotations of the input string
    rotations = [input_string[i:] + input_string[:i] for i in range(len(input_string))]

    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)

    # Extract the last characters of each sorted rotation to form the BWT
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)

    # Find the index of the original string in the sorted rotations
    original_index = sorted_rotations.index(input_string)

    return bwt_result, original_index

def inverse_burrows_wheeler_transform(bwt_string, original_index):
    matrix = sorted([(char, i) for i, char in enumerate(bwt_string)])

    # Reconstruct the original string from the sorted matrix
    original_string = ''
    for _ in range(len(bwt_string)):
        original_string = matrix[original_index][0] + original_string
        original_index = matrix[original_index][1]

    return original_string.rstrip('\0')[::-1]

# Example usage
original_text = "abracadabra"

# Apply Burrows-Wheeler Transform
bwt_result, original_index = burrows_wheeler_transform(original_text)
print("Burrows-Wheeler Transform:", bwt_result)
print("Original Index:", original_index)

# Inverse Burrows-Wheeler Transform to get back the original string
inverse_result = inverse_burrows_wheeler_transform(bwt_result, original_index)
print("Inverse Burrows-Wheeler Transform:", inverse_result)
