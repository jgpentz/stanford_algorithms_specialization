from collections import defaultdict

def read_data(g_idx):
    '''
    Reads in a the vertices and edges from a graph

    Returns:
        directed graph with the start vertices as keys and the end vertices
        and the weight stored as tuples for the values

        Note: some vertices may not be connected
    '''
    graph = defaultdict(list)
    num_vertices = 0

    with open(f'g{g_idx}.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                num_vertices = int(line.strip().split(' ')[0])
                continue
            a, b, weight = line.strip().split(' ')
            graph[int(a)].append((int(b), int(weight)))

    return graph, num_vertices


def floyd_warshall(g, num_vertices):
    '''
    Compute the shortest path between each pair of points

    :param g: graph with vertices and edges
    :param num_vertices: number of vertices in graph

    Returns:
        the value of the shortest path, or float('inf') if there is neg cycle
    '''
    shortest_path = float('inf')

    # Base cases: 0 if v == w, l_vw if (v, w) is an edge of G, inf if (v, w)
    # is not an edge of G
    distances = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]
    for v in g:
        distances[v - 1][v - 1] = 0
        for end_v, weight in g[v]:
            if weight < shortest_path:
                shortest_path = weight
            distances[v - 1][end_v - 1] = weight

    # Loop through each pair or vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

                    # Check shortest path
                    if distances[i][k] + distances[k][j] < shortest_path:
                        shortest_path = distances[i][k] + distances[k][j]


    # Check for negative cycles along the diagonal
    for v in range(num_vertices):
        if distances[v][v] < 0:
            return float('inf')

    return shortest_path


if __name__ == "__main__":
    for g_idx in range(1, 4):
        g, num_vertices = read_data(g_idx)
        print(floyd_warshall(g, num_vertices))

