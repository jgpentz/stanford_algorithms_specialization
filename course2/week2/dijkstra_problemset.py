import os
from collections import defaultdict

def get_graph():
    g = defaultdict(list)
    with open(f'{str(os.getcwd())}/course2/week2/dijkstraData.txt') as f:
    # with open(f'{str(os.getcwd())}/course2/week2/test.txt') as f:
        for line in f:
            line = line.strip().split('\t')
            for i in range(1, len(line)):
                edge, weight = line[i].split(',')
                weight = int(weight)
                g[line[0]].append((edge, weight))

    return g


def djikstras(g, start, end):
    x = [start]
    a = {start: 0}

    while end not in x:
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

    # print(x, a)
    path = [node for node in a]
    dist = a[end]
    return path, dist

if __name__ == "__main__":
    g = get_graph()
    end_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    # print(g)
    distances = []
    for end_vertex in end_vertices:
        path, dist = djikstras(g, str(1), str(end_vertex))
        distances.append(dist)
        print(f'Dist: {dist}')
    print(distances)