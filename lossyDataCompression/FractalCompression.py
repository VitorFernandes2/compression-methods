import pyfractal

# Load the image
image = pyfractal.load_image("input.jpg")

# Perform fractal compression
compressed_data = pyfractal.compress(image)

# Save the compressed data to a file
pyfractal.save_compressed_data(compressed_data, "compressed.fractal")

# Load the compressed data from the file
compressed_data = pyfractal.load_compressed_data("compressed.fractal")

# Decompress the data
reconstructed_image = pyfractal.decompress(compressed_data)

# Save the reconstructed image
pyfractal.save_image(reconstructed_image, "output.jpg")
