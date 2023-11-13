def lz78_compress(data):
    dictionary = {0: ''}
    compressed_data = []
    current_phrase = ''

    for symbol in data:
        current_phrase += symbol
        if current_phrase not in dictionary:
            dictionary[current_phrase] = len(dictionary)
            if len(current_phrase) == 1:
                compressed_data.append((0, symbol))
            else:
                compressed_data.append((dictionary[current_phrase[:-1]], symbol))
            current_phrase = ''

    if current_phrase:
        compressed_data.append((dictionary[current_phrase], ''))

    return compressed_data


def lz78_decompress(compressed_data):
    dictionary = {0: ''}
    decompressed_data = []

    for index, symbol in compressed_data:
        if index in dictionary:
            phrase = dictionary[index] + symbol
        else:
            raise ValueError("Invalid dictionary index.")

        decompressed_data.append(phrase)
        dictionary[len(dictionary)] = phrase

    return ''.join(decompressed_data)

# Example usage
data = "abracadabra"
compressed_data = lz78_compress(data)
print("Compressed data:", compressed_data)

decompressed_data = lz78_decompress(compressed_data)
print("Decompressed data:", decompressed_data)
