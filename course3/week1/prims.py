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

            graph[vertex_a][vertex_b] = weight

    return graph


def prims(graph):
    mst = defaultdict(dict)
    visited = []




if __name__ == "__main__":
    graph = read_data()