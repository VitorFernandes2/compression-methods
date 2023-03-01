from collections import OrderedDict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

def LengthEncoding(input):
    list = []
    list_size=0
    for ch in input:
        if list_size == 0:
            list.append(Node(ch, 1))
            list_size += 1
        else:
            node = list[list_size - 1]
            if node.key == ch:
                node.value += 1 
            else:
                list.append(Node(ch, 1))
                list_size += 1

    output = ''
    for node in list:
        output = output + node.key + str(node.value)
    return output
