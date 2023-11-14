from collections import deque

def ucc(g):
    explored = {}
    numCC = 0
    for i in g:
        if i not in explored:
            numCC += 1
            q = deque()
            q.append(i)
            explored[i] = numCC
            while q:
                cur_v = q.popleft()
                for v in g[cur_v]:
                    if v not in explored:
                        explored[v] = numCC
                        q.append(v)
    print(explored)

if __name__ == "__main__":
    # Graph G:
    # 
    #         --- 2 --- 4       6     7 --- 8       -- 10 ---
    #       /          / \     /                  /           \
    #     1           /   \   /                 9              12
    #      \         /     \ /                   \            /
    #       ------- 3 ----- 5                     ---- 11 ---
    # 
    g_ucc = {
        # Component 1
        1: [2, 3],
        2: [1, 4],
        3: [1, 4, 5],
        4: [2, 3, 5],
        5: [3, 4, 6],
        6: [5],
        # Component 2
        7: [8],
        8: [7],
        # Component 3
        9: [10, 11],
        10: [9, 12],
        11: [9, 12],
        12: [10, 11],
    }

    ucc(g_ucc)