from collections import deque
import os


def read_data():
    '''
    Reads in symbols (line numbers) and their weights (frequency)

    Returns:
        List of tuples of the weight and symbol e.g. (104, 0) corresponds
        to symbol 0 with a weight of 104
    '''
    symbols = []

    with open(f'{str(os.getcwd())}/course3/week3/huffman.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            symbol = ''.join(line.strip().split(' '))
            symbols.append((int(symbol), i))

    return symbols


class Node():
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight
        self.left = None
        self.right = None

class Huffman():
    def __init__(self, symbols):
        self.root = None

        symbols.sort()
        symbol_queue = deque()
        combo_queue = deque()
        for i in range(len(symbols)):
            symbol_queue.append(Node(symbols[i][1], symbols[i][0]))

        while (len(symbol_queue) + len(combo_queue)) > 1:
            merged_nodes = []
            for i in range(2):
                if len(symbol_queue) == 0:
                    merged_nodes.append(combo_queue.popleft())
                elif len(combo_queue) == 0:
                    merged_nodes.append(symbol_queue.popleft())
                else:
                    if symbol_queue[0].weight < combo_queue[0].weight:
                        merged_nodes.append(symbol_queue.popleft())
                    else:
                        merged_nodes.append(combo_queue.popleft())

            self.root = Node(None, (merged_nodes[0].weight + merged_nodes[1].weight))
            self.root.left = merged_nodes[0]
            self.root.right = merged_nodes[1]

            combo_queue.append(self.root)

    def max_depth(self):
        return self._max_depth(self.root)

    def _max_depth(self, root):
        if root == None:
            return 0
        
        ldepth = self._max_depth(root.left)
        rdepth = self._max_depth(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1
        
    def min_depth(self):
        return self._min_depth(self.root)
    
    def _min_depth(self, root):
        q = deque()
        q.append((root, 1))

        while q:
            item = q.popleft()
            node = item[0]
            depth = item[1]

            if node.left is None and node.right is None:
                return depth
            
            if node.left is not None:
                q.append((node.left, depth + 1))

            if node.right is not None:
                q.append((node.right, depth + 1))

if __name__ == "__main__":
    symbols = read_data()
    h = Huffman(symbols)
    print(f"Max depth: {h.max_depth() - 1}")
    print(f"Min depth: {h.min_depth() - 1}")