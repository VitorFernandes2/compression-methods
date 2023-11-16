def delta_encode(double_values):
    if not double_values:
        return []

    encoded_values = [double_values[0]]
    for i in range(1, len(double_values)):
        delta = double_values[i] - double_values[i - 1]
        encoded_values.append(round(delta, 2))

    return encoded_values

def delta_decode(encoded_values):
    if not encoded_values:
        return []

    decoded_values = [encoded_values[0]]
    for i in range(1, len(encoded_values)):
        value = decoded_values[i - 1] + encoded_values[i]
        decoded_values.append(value)

    return decoded_values
