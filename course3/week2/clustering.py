import os

def read_data():
    '''
    Reads in a list of edges, and stores them in an adjacency list graph.

    Returns:
    '''
    edges = []

    with open(f'{str(os.getcwd())}/course3/week2/edges.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                num_vertices = int(line.strip())
                continue
            vertex_a, vertex_b, weight = line.strip().split(' ')
            edges.append((int(weight), int(vertex_a) - 1, int(vertex_b) - 1))

    return edges, num_vertices

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
    

def kruskals(edges, num_vertices):
    num_clusters = num_vertices
    edges.sort()
    uf = UnionFind(num_vertices)

    for iedge in range(len(edges)):
        vertex_a = edges[iedge][1]
        vertex_b = edges[iedge][2]
        if uf.union(vertex_a, vertex_b):
            num_clusters -= 1
            if num_clusters == 4:
                # Max spacing: finish the clustering algorithm, and then
                # compute once more for the closest pair of separate (i.e., 
                # from different clusters) points. This edge will be your 
                # maximum spacing.
                for weight, vertex_a, vertex_b in edges[(iedge + 1):]:
                    if uf.find(vertex_a) != uf.find(vertex_b):
                        return weight
            

if __name__ == "__main__":
    edges, num_vertices = read_data()
    print(kruskals(edges, num_vertices))