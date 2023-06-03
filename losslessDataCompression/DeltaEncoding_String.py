def delta_encode_string(data):
    encoded_data = [data[0]]  # Start with the first character as it is

    for i in range(1, len(data)):
        diff = ord(data[i]) - ord(data[i-1])  # Calculate the character difference
        encoded_data.append(diff)

    return encoded_data

def delta_decode_string(encoded_data):
    data = [encoded_data[0]]  # Start with the first character as it is

    for i in range(1, len(encoded_data)):
        char_code = ord(data[i-1]) + encoded_data[i]  # Add the character difference to the previous character's code
        char = chr(char_code)  # Convert the character code back to a character
        data.append(char)

    return ''.join(data)

data = "abracadabra"
encoded_data = delta_encode_string(data)
print("Encoded data:", encoded_data)

decoded_data = delta_decode_string(encoded_data)
print("Decoded data:", decoded_data)
