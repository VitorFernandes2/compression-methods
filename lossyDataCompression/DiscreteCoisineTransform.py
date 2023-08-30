import numpy as np
from scipy.fftpack import dct, idct

def dct2(block):
    return dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')

def idct2(coefficients):
    return idct(idct(coefficients, axis=0, norm='ortho'), axis=1, norm='ortho')

# Example usage
block = np.array([[154, 123, 123, 123, 123, 123, 123, 136],
                  [192, 180, 136, 154, 154, 154, 136, 110],
                  [254, 198, 154, 154, 180, 154, 123, 123],
                  [239, 180, 136, 180, 180, 166, 123, 123],
                  [180, 154, 136, 167, 166, 149, 136, 136],
                  [128, 136, 123, 136, 154, 180, 198, 154],
                  [123, 105, 110, 149, 136, 136, 180, 166],
                  [110, 136, 123, 123, 123, 136, 154, 136]])

dct_block = dct2(block)
reconstructed_block = idct2(dct_block)

print("Original Block:")
print(block)
print("\nDCT Coefficients:")
print(dct_block)
print("\nReconstructed Block:")
print(reconstructed_block.round().astype(int))
