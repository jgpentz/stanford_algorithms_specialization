from collections import deque

explored = set()

def dfs(g, start_vertex):
    print(start_vertex)
    explored.add(start_vertex)
    for edge in g[start_vertex]:
        if edge not in explored:
            dfs(g, edge)

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
        'E': ['C', 'D'],
    }

    dfs(g, 'S')
    print(explored)
    