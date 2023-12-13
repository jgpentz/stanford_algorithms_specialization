from collections import defaultdict
import sys

sys.setrecursionlimit(2**20)

explored = set()
finishing_times = []
scc = {}
scc_idx = 0


def read_data(file):
    '''
    Reads in cities and their x, y coordinates

    Returns:
        list of cities identified by a tuple of their x, y coordinates
    '''
    clauses = []

    with open(f'{file}.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            x, y  = line.strip().split(' ')
            clauses.append((int(x), int(y)))

    return clauses


def build_implications(clauses):
    '''
    Constructs an implication graph and its' transpose based on a set of clauses
    '''
    adj = defaultdict(list)
    adj_t = defaultdict(list)

    for clause in clauses:
        # Normal implciation graph
        adj[-1 * clause[0]].append(clause[1])
        adj[-1 * clause[1]].append(clause[0])

        # Reversed implication graph
        adj_t[clause[1]].append(-1 * clause[0])
        adj_t[clause[0]].append(-1 * clause[1])

    return adj, adj_t


def dfs1(g, s):
    '''
    DFS for computing finishing times
    '''
    global explored
    global finishing_times

    explored.add(s)

    # Note: Need to check if s is in g because the next line will create
    # a new entry in the defaultdict if the key isn't present
    if s in g:
        for v in g[s]:
            if v not in explored:
                dfs1(g, v)

    finishing_times.append(s)


def dfs1_loop(g):
    '''
    Computes the depth first search finishing times of a graph
    '''
    global explored
    
    for v in g:
        if v not in explored:
            dfs1(g, v)


def dfs2(g_r, s):
    '''
    DFS for computing scc
    '''
    global scc
    global scc_idx

    scc[s] = scc_idx

    for v in g_r[s]:
        if v not in scc:
            dfs2(g_r, v)


def dfs2_loop(g_r):
    '''
    Computes the strongly connected components of a graph
    '''
    global scc
    global scc_idx
    global finishing_times

    while finishing_times:
        v = finishing_times.pop()
        if v not in scc:
            scc_idx += 1
            dfs2(g_r, v)


def solve_2sat():
    '''
    Checks if key x is in the same scc as ~x
    '''
    global scc

    for k, _ in scc.items():
        if scc[k] == scc[-1 * k]:
            return False
    
    return True


if __name__ == "__main__":
    soln = ''
    for i in range(1, 7):
        # Set default global values
        explored = set()
        finishing_times = []
        scc = {}
        scc_idx = 0

        # Calculate 2 sat
        clauses = read_data(f'2sat{i}')
        adj, adj_t = build_implications(clauses)
        dfs1_loop(adj)
        dfs2_loop(adj_t)
        if solve_2sat():
            soln += '1'
        else:
            soln += '0'

    print(soln)

