import pandas as pd

# Sample dataset
data = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Green', 'Red']})

# Perform one-hot encoding
encoded_data = pd.get_dummies(data)

print("Original data:")
print(data)

print("\nEncoded data:")
print(encoded_data)
