class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            return True
        return False
    
def kruskals(edges, num_nodes):
    uf = UnionFind(num_nodes)
    mst = []
    edges.sort()
    edge_count = 0
    min_weight = 0

    for weight, node_a, node_b in edges:
        if uf.union(node_a, node_b):
            min_weight += weight
            edge_count += 1
            mst.append((node_a, node_b))
            if edge_count == num_nodes - 1:
                print(mst)
                return min_weight

if __name__ == "__main__":
    edges = [
        # weight, node1, node2
        [2, 0, 2],
        [6, 0, 3],
        [5, 1, 2],
        [1, 1, 4],
        [2, 2, 3],
        [3, 3, 4],
    ]
    numOfNodes = 5
    print("min total weight:", kruskals(edges, numOfNodes))