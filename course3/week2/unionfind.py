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

        return

# Example usage:
uf = UnionFind(10)

print("Initial parent array:", uf.parent)

uf.union(0, 3)
uf.union(0, 2)
uf.union(3, 1)

uf.union(4, 5)
uf.union(5, 0)

uf.union(6, 7)
uf.union(6, 8)
uf.union(7, 9)

uf.union(1, 7)

print("Parent array after unions:", uf.parent)

print("Representative of set containing 2:", uf.find(2))
print("Representative of set containing 3:", uf.find(3))