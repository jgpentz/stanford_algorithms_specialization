from collections import deque

def bfs(g, s):
    explored = {}
    queue = deque()
    queue.append(s)
    explored[s] = 0

    # Pop an item off the queue, search through its' adjacent nodes,
    # If any of the nodes are unexplored, mark it as explored and 
    # add it to the queue
    while queue:
        current_node = queue.popleft()
        for node in g[current_node]:
            if node not in explored:
                explored[node] = explored[current_node] + 1
                queue.append(node)

    print(explored)

          

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

    bfs(g, 'S')
    