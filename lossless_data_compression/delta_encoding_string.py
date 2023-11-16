def delta_encode_strings(strings):
    deltas = []
    previous_string = strings[0]

    for current_string in strings[1:]:
        delta = ""
        min_len = min(len(previous_string), len(current_string))

        for i in range(min_len):
            if previous_string[i] != current_string[i]:
                delta += current_string[i]
            else:
                delta += '\0'  # Placeholder for unchanged characters

        if len(current_string) > len(previous_string):
            delta += current_string[min_len:]
        deltas.append(delta)
        previous_string = current_string

    return deltas

def delta_decode_strings(encoded_strings):
    decoded_strings = []
    previous_string = ''

    for delta in encoded_strings:
        current_string = ""
        for char in delta:
            if char == '\0':
                current_string += previous_string[len(current_string)]
            else:
                current_string += char
        decoded_strings.append(current_string)
        previous_string = current_string

    return decoded_strings
