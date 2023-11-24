import heapq
from collections import defaultdict

def mst(graph):
    start = list(graph.keys())[0]
    visited = set()
    tree = defaultdict(dict)

    pq = [(0, None, start)]

    while pq:
        # Take the smallest edge off the pq
        curr_weight, head, tail = heapq.heappop(pq)

        # Don't need to look at same vertex twice
        if tail in visited:
            continue

        visited.add(tail)
        tree[head][tail] = curr_weight

        # Explore the neighbors
        for neighbor, weight in graph[tail].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, tail, neighbor))

    return tree


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
graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'C': 3},
    'C': {}
}
tree = mst(graph)
print(tree)