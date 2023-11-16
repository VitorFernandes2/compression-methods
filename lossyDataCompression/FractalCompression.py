import numpy as np
import utils.dataset_operations as ds_utils
import utils.DatasetsConstants as constants
import os

# Generate a synthetic 2D numeric dataset
original_ds = os.getcwd() + constants.TIMESERIES_MONTHLY_BEER_PRODUCTION_PATH

ds = ds_utils.convertDateColumnToTimeseries(
    0, 1, ds_utils.readNumberArrayFromDataset(original_ds), format="%Y-%m")

original_data = np.array(ds)

# Function to divide a dataset into non-overlapping blocks
def divide_dataset(data, block_size):
    rows, cols = data.shape
    divided_data = []
    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            block = data[i:i + block_size, j:j + block_size]
            divided_data.append(block)
    return divided_data

# Function to find the best-matching block using mean squared error (MSE)
def find_best_match(target_block, candidate_blocks):
    best_mse = float('inf')
    best_match = None
    for block in candidate_blocks:
        mse = np.mean((target_block[:,None] - block) ** 2)
        if mse < best_mse:
            best_mse = mse
            best_match = block
    return best_match

# Compression parameters
block_size = 32  # Adjust block size as needed
encoded_data = []

# Divide the dataset into blocks
blocks = divide_dataset(original_data, block_size)

# Iterate through the blocks and find best-matching patterns
for block in blocks:
    best_match = find_best_match(block, blocks)
    encoded_data.append(best_match)

# Reconstruct the dataset using the encoded data
reconstructed_data = np.vstack(encoded_data).reshape(original_data.shape)

# Calculate compression ratio
original_size = original_data.size * original_data.itemsize
compressed_size = len(encoded_data) * block_size**2 * original_data.itemsize
compression_ratio = original_size / compressed_size

print(f"Compression Ratio: {compression_ratio:.2f}")

# Compare the original and reconstructed datasets (for demonstration purposes)
mse = np.mean((original_data - reconstructed_data) ** 2)
print(f"Mean Squared Error (MSE) between original and reconstructed data: {mse:.4f}")
