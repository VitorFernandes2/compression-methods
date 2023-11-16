def compress(data):
    compressed_data = []
    index = 0

    while index < len(data):
        longest_match = ''
        for i in range(1, min(index, len(data) - index)):
            substring = data[index:index + i]
            if substring in data[:index]:
                longest_match = substring
            else:
                break

        if longest_match:
            distance = index - data.rfind(longest_match, 0, index)
            next_char = data[index + len(longest_match)]
            compressed_data.append((distance, len(longest_match), next_char))
            index += len(longest_match) + 1
        else:
            compressed_data.append((0, 0, data[index]))
            index += 1

    return compressed_data

def decompress(compressed_data):
    decompressed_data = ''
    for (distance, length, next_char) in compressed_data:
        if distance == 0:
            decompressed_data += next_char
        else:
            start_index = len(decompressed_data) - distance
            repeated_string = decompressed_data[start_index:start_index + length]
            decompressed_data += repeated_string + next_char

    return decompressed_data
