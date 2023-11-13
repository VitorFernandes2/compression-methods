def delta_encode(data):
    encoded_data = [data[0]]  # Start with the first element as it is

    for i in range(1, len(data)):
        diff = data[i] - data[i-1]  # Calculate the difference
        encoded_data.append(diff)

    return encoded_data

def delta_decode(encoded_data):
    data = [encoded_data[0]]  # Start with the first element as it is

    for i in range(1, len(encoded_data)):
        value = data[i-1] + encoded_data[i]  # Add the difference to the previous value
        data.append(value)

    return data

data = [10, 14, 18, 22, 26]
encoded_data = delta_encode(data)
print("Encoded data:", encoded_data)

decoded_data = delta_decode(encoded_data)
print("Decoded data:", decoded_data)
