import heapq
from collections import defaultdict

def prims(graph):
    start = list(graph.keys())[0]
    mst = defaultdict(dict)
    visited = set()

    pq = [(0, start, None)]

    while pq:
        # Take the vertex with the shortest edge out of pw
        curr_weight, curr_vertex, parent = heapq.heappop(pq)

        if curr_vertex in visited:
            continue

        visited.add(curr_vertex)

        if parent is not None:
            mst[parent][curr_vertex] = curr_weight

        for neighbor, weight in graph[curr_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, curr_vertex))

    return mst


# Example usage:
graph = {
    'A': {'B': 8, 'C': 3, 'D': 6},
    'B': {'A': 8, 'E': 5},
    'C': {'A': 3, 'D': 2},
    'D': {'A': 6, 'C': 2, 'E': 5, 'G': 3},
    'E': {'B': 5, 'D': 5, 'F': 5},
    'F': {'E': 5, 'G': 3, 'H': 6},
    'G': {'D': 3, 'F': 3, 'H': 4},
    'H': {'F': 6, 'G': 4},
}
tree = prims(graph)
print(tree)