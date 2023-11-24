import heapq
from collections import Counter, namedtuple

# Node class for building the Huffman tree
class Node:
    def __init__(self, frequency, char=None, left=None, right=None):
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to build the Huffman tree
def build_tree(frequencies):
    heap = [Node(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, parent)

    return heap[0]

# Function to generate Huffman codes for each character in the tree
def generate_codes(node, code='', codes={}):
    if node.char:
        codes[node.char] = code
    else:
        generate_codes(node.left, code + '0', codes)
        generate_codes(node.right, code + '1', codes)

    return codes

# Function to encode the input string using the generated Huffman codes
def encode(data, codes):
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    return encoded_data

# Function to decode the Huffman-encoded data using the Huffman tree
def decode(encoded_data, tree):
    decoded_data = ''
    node = tree
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right

        if node.char:
            decoded_data += node.char
            node = tree

    return decoded_data
