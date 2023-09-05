from collections import defaultdict
import random
from copy import deepcopy

def get_graph():
    graph = defaultdict(list)

    # Store each row into the graph object:
    # First column in each row is the vertex,
    # all remaining columns in the row are the adjacent vertices (edges)
    for line in open('./kargermincut.txt'):
        line = line.strip()
        row = [int(n) for n in line.split('\t')]
        for i in range(1, len(row)):
            graph[row[0]].append(row[i])

    return graph

def karger(graph):
    while len(graph) > 2:
        # Choose a random edge to fuse
        vertex = random.choice(list(graph))
        merge_vertex = graph[vertex].pop(random.randrange(len(graph[vertex])))

        # Merge the other edge into this one, updating all references
        # in other nodes
        merge_adjacencies = graph.pop(merge_vertex, None)
        for adj in merge_adjacencies:
            graph[adj][:] = [vertex if x == merge_vertex else x for x in graph[adj]]
        graph[vertex] += merge_adjacencies

        # Remove self loop
        # Note: the [:] performs a slice assignment (replaces old list with new list, same memory)
        graph[vertex][:] = [x for x in graph[vertex] if x != vertex and x != merge_vertex]
    
    # Return the mincut
    mincut = len(graph[list(graph)[0]])
    return(mincut)


if __name__ == "__main__":
    graph = get_graph()
    lowest_mincut = karger(deepcopy(graph))
    for i in range(20):
        mincut = karger(deepcopy(graph))
        if mincut < lowest_mincut:
            lowest_mincut = mincut
        print(mincut)
    print(f'lowest min cut: {lowest_mincut}')
        