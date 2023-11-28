from collections import defaultdict
explored = set()
f_time = []
scc = defaultdict(list)
leader = 0

def dfs_loop1(g):
    global explored
    for i in range(max(g), 0, -1):
        if i not in explored:
            dfs1(g, i)

def dfs1(g, s):
    global explored
    global f_time
    explored.add(s)
    for v in g[s]:
        if v not in explored:
            dfs1(g,v)
    f_time.append(s)

def dfs_loop2(g):
    global leader
    global explored
    global f_time
    explored = set()
    while f_time:
        v = f_time.pop()
        if v not in explored:
            leader = v
            dfs2(g, v)

def dfs2(g, s):
    global scc
    global explored
    global leader
    explored.add(s)
    for v in g[s]:
        if v not in explored:
            dfs2(g, v)
    scc[leader].append(s)

def graph_reverse(g):
    g_rev = defaultdict(list)
    for k, v in g.items():
        for i in v:
            g_rev[i].append(k)

    return g_rev

if __name__ == '__main__':
    g= {
        1: [4],
        2: [8],
        3: [6],
        4: [7],
        5: [2],
        6: [9],
        7: [1],
        8: [5,6],
        9: [3,7],
    }
    g_rev = graph_reverse(g)
    dfs_loop1(g_rev)
    dfs_loop2(g)
    print(scc)
