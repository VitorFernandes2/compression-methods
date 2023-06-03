class AdaptiveHuffmanNode:
    def __init__(self, weight, symbol=None, parent=None, left=None, right=None):
        self.weight = weight
        self.symbol = symbol
        self.parent = parent
        self.left = left
        self.right = right
        self.is_new = True

    def is_leaf(self):
        return self.symbol is not None


class AdaptiveHuffmanEncoder:
    def __init__(self):
        self.root = AdaptiveHuffmanNode(0)
        self.nodes = [self.root]
        self.code_table = {}

    def _update_tree(self, node):
        while node.parent is not None:
            parent = node.parent
            min_node = min(self.nodes, key=lambda x: (x.weight, x.symbol is None, x.is_new))
            if node is not min_node:
                node_index = self.nodes.index(node)
                min_index = self.nodes.index(min_node)
                self.nodes[node_index], self.nodes[min_index] = self.nodes[min_index], self.nodes[node_index]
                if parent.left is node:
                    parent.left, parent.right = parent.right, parent.left
            parent.weight += 1
            node.weight += 1
            node.is_new = False
            node = parent

    def _add_node(self, symbol):
        new_node = AdaptiveHuffmanNode(1, symbol, parent=self.nodes[0])
        self.nodes.append(new_node)
        if self.nodes[0].left is None:
            self.nodes[0].left = new_node
        else:
            self.nodes[0].right = new_node
        self._update_tree(new_node)
        return new_node

    def _get_code(self, node):
        code = ''
        while node.parent is not None:
            if node is node.parent.left:
                code = '0' + code
            else:
                code = '1' + code
            node = node.parent
        return code

    def encode(self, data):
        encoded_data = ''
        for symbol in data:
            if symbol in self.code_table:
                code = self.code_table[symbol]
            else:
                code = self._get_code(self._add_node(symbol))
                self.code_table[symbol] = code
            encoded_data += code
        return encoded_data


# Example usage
encoder = AdaptiveHuffmanEncoder()
data = "abracadabra"
encoded_data = encoder.encode(data)

print("Original data:", data)
print("Encoded data:", encoded_data)
