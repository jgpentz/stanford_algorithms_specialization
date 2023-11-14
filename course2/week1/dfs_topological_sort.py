cur_label = 0 
explored = {}
def topo_sort(g):
    global cur_label
    cur_label = len(g)
    for v in g.keys():
        if v not in explored:
            dfs_topo(g, v)

def dfs_topo(g, s):
    global cur_label
    explored[s] = float('inf')
    for v in g[s]:
        if v not in explored:
            dfs_topo(g, v)

    explored[s] = cur_label
    cur_label -= 1

if __name__ == "__main__":
    # Graph G:
    # 
    #         --> 2 --> 4 ----> 6
    #       /          ^       ^
    #     1           /       /
    #      \         /       /
    #       ------> 3 ----> 5
    # 

    # Directed acyclic graph
    g = {
        # Component 1
        1: [2, 3],
        2: [4],
        3: [4, 5],
        4: [6],
        5: [6],
        6: [],
    }
    topo_sort(g)
    print(explored)