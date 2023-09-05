from collections import defaultdict
import random
from copy import deepcopy
from collections import deque

def bfs(g):
    explored = []
    explored.append('S')
    levels = defaultdict(list)
    level = 0
    levels[level].append('S')

    q = deque()
    q.append('S')

    while q:
        node = q.popleft()
        level += 1
        for adj_node in g[node]:
            if adj_node not in explored:
                explored.append(adj_node)
                q.append(adj_node)
                levels[level].append(adj_node)

    print(levels)



# if __name__ == "__main__":
#     a = [9, 3, 7, 5, 6, 4, 8, 2, 1, 10]
#     # print(quicksort(a, 0, len(a) - 1))
#     for kth in range(1, (len(a) + 1)):
#         print(quickselect(a, kth, 0, len(a) - 1))

if __name__ == "__main__":
    # Graph G:
    # 
    #         --- A --- C ----- E
    #       /          / \     /
    #     S           /   \   /
    #      \         /     \ /
    #       ------- B ----- D 
    # 

    g = {
        'S': ['A', 'B'],
        'A': ['S', 'C'],
        'B': ['S', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }

    bfs(g)
    