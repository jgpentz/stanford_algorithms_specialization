from collections import defaultdict, Counter
import os, sys, resource

# Setting recursion limit because the default depth is 1000
sys.setrecursionlimit(2**20)

explored = set()
finishing_times = []
leaders = {}
leader = 0
sccs = {}


def load_data():
    graph = defaultdict(list)
    graph_r = defaultdict(list)
    max_node = -1

    # Store each row into the graph object:
    # First column in each row is the vertex,
    # all remaining columns in the row are the adjacent vertices (edges)
    with open(f'{str(os.getcwd())}/course2/week1/scc.txt') as f:
        for line in f:
            from_node, to_node = line.strip().split(' ')
            from_node, to_node = int(from_node), int(to_node)
            graph[from_node].append(to_node)
            graph_r[to_node].append(from_node)

            if from_node > max_node:
                max_node = from_node

    return graph, graph_r, max_node


def dfs1(g, start_node):
    explored.add(start_node)
    for edge in g[start_node]:
        if edge not in explored:
            dfs1(g, edge)
    
    # Add finishing time to the stack
    global finishing_times
    finishing_times.append(start_node)

def dfs_loop1(graph_r, max_node):
    for i in range(max_node, 0, -1):
        if i not in explored:
            global leader
            leader = i
            dfs1(graph_r, i)


def dfs2(g, start_node):
    global leaders
    explored.add(start_node)
    leaders[leader] = 1 + leaders.get(leader, 0)
    for edge in g[start_node]:
        if edge not in explored:
            dfs2(g, edge)


def dfs_loop2(graph, max_node):
    # Reset explored since we're going through the graph in whole again,
    # and reset leaders because it didn't mean anything in the first pass
    global explored
    global leaders
    global leader
    explored = set()
    leaders = {}

    while finishing_times:
        leader = finishing_times.pop()
        if leader not in explored:
            dfs2(graph, leader)


if __name__ == "__main__":
    graph, graph_r, max_node = load_data()
    dfs_loop1(graph_r, max_node)
    dfs_loop2(graph, max_node)

    # Print the top 5
    counter = Counter(leaders)
    top5 = counter.most_common(5)
    for i in top5:
        print(i[1])