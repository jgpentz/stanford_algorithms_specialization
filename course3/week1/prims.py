from collections import defaultdict
import heapq
import os

def read_data():
    '''
    Reads in a list of edges, and stores them in an adjacency list graph.

    Returns:
        graph {
            vertex_a: {
                vertex_b: weight, 
                vertex_c: weight
            },
            vertex_b: {
                vertex_d: weight,
                vertex_e: weight
            }
        }
    '''
    graph = defaultdict(dict)
    
    with open(f'{str(os.getcwd())}/course3/week1/edges_data.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            vertex_a, vertex_b, weight = line.strip().split(' ')
            vertex_a, vertex_b, weight = int(vertex_a), int(vertex_b), int(weight)

            # Both vertices contain this edge since it's an undirected graph
            graph[vertex_a][vertex_b] = weight
            graph[vertex_b][vertex_a] = weight

    return graph


def prims(graph):
    '''
    Iterates through a graph, looking at each edge and selecting the edge between two
    vertices that has the smallest weight.  It grows like a mold until all vertices
    have been accounted for, which results in a minimum spanning tree (mst).  Both the
    mst and the overall cost of the mst are returned.
    '''
    mst = defaultdict(dict)
    visited = set()
    total_cost = 0

    # Create a priority queue that stores keys as tuples of the order:
    # (weight, current vertex, parent vertex)
    # Note: start vertex can be any vertex, but it's arbitrarily chosen as 1
    pq = [(0, 1, None)]

    while pq:
        # Pull off the next vertex with the smallest edge weight
        new_weight, current_vertex, parent_vertex = heapq.heappop(pq)

        # Skip vertices that have already been explored
        if current_vertex in visited:
            continue

        # Mark this as visited, and increment the running total cost
        visited.add(current_vertex)
        total_cost += new_weight

        # Store this new edge in the mst
        if parent_vertex is not None:
            mst[parent_vertex][current_vertex] = new_weight
            mst[current_vertex][parent_vertex] = new_weight

        # Check all neighboring vertices and add any new ones to the heap
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, current_vertex))

    return mst, total_cost


if __name__ == "__main__":
    graph = read_data()
    mst, total_cost = prims(graph)

    print(f"Total cost of mst is: {total_cost}")