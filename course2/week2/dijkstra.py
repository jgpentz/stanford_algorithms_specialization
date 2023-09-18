def djikstras(g, start):
    x = [start]
    a = {start: 0}

    while 't' not in x:
        current_lowest = None
        for node in x:
            for edge in g[node]:
                if edge[0] not in x:
                    if current_lowest == None:
                        current_lowest = (edge[0], a[node] + edge[1])
                    elif a[node] + edge[1] < current_lowest[1]:
                        current_lowest = (edge[0], a[node] + edge[1])                        
        x.append(current_lowest[0])
        a[current_lowest[0]] = current_lowest[1]

    print(x, a)

    return

if __name__ == "__main__":
    #    --- 1 --> v --- 6 --
    #  /           |          \
    # s            2           t
    #  \           |           /
    #   \          v          /
    #    --- 4 --- w --- 3 --

    g = {
        's': [('v', 1), ('w', 4)],
        'v': [('x', 10), ('w', 2), ('t', 6)],
        'x': [('t', 10)],
        'w': [('t', 3)],
        't' : []
    }
    djikstras(g, 's')