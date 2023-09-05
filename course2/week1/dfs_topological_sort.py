explored = set()
finishing_times = {}
current_label = 0

def dfs(g, start_node):
    print(start_node)
    explored.add(start_node)
    for edge in g[start_node]:
        if edge not in explored:
            dfs(g, edge)
    
    # Register the current topological ordering
    global current_label
    finishing_times[start_node] = current_label
    current_label -= 1


if __name__ == "__main__":
    # Graph G:
    # 
    #         --> A --> C ----> E
    #       /          ^       ^
    #     S           /       /
    #      \         /       /
    #       ------> B ----> D 
    # 

    # Directed acyclic graph
    g = {
        'S': ['A', 'B'],
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['E'],
        'E': [],
    }
    current_label = len(g)

    for node in g:
        if node not in explored:
            dfs(g, node)
    print(finishing_times)
    