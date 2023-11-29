
import os
from collections import defaultdict
import itertools

def read_data():
    '''
    Reads in a list of edges, and stores them in an adjacency list graph.

    Returns:
    '''
    numbers = []

    with open(f'{str(os.getcwd())}/course3/week2/edges_big.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            bits = ''.join(line.strip().split(' '))
            number = int(bits, 2)
            numbers.append(number)

    return numbers

class UnionFind():
    def __init__(self, num_vertices):
        self.parent = [i for i in range(num_vertices)]
        self.rank = [0] * num_vertices

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression

        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

            return True
        
        return False
    

def clustering(numbers):
    nodes = defaultdict(list)
    uf = UnionFind(len(numbers))

    # Store a mapping of all numbers to a list of the nodes (line number) with
    # that value
    for node, num in enumerate(numbers):
        nodes[num].append(node)
    
    # Create bit masks for all bit combinations that are distance 1 and distance
    # 2 away from the current node
    distances = [1 << i for i in range(24)]
    distances += [((1 << i) | (1 << j)) for i, j in itertools.combinations(range(24), 2)]
    distances += [0]

    k = len(numbers)
    for distance in distances:
        for number in nodes.keys():
            if (number ^ distance) in nodes:
                for node_a in nodes[number]:
                    for node_b in nodes[number ^ distance]:
                        if(uf.union(node_a, node_b)):
                            k -= 1

    return k


if __name__ == "__main__":
    numbers = read_data()
    print(clustering(numbers))