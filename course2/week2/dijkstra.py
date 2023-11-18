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


# import heapq

# def dijkstra(graph, start):
#     # Initialzie distances and predecessors
#     distances = {vertex: float('inf') for vertex in graph}
#     predecessors = {vertex: None for vertex in graph}
#     distances[start] = 0

#     # Create a riority q to store vertices and their distances
#     pq = [(0, start)]

#     while pq:
#         # Get the vertex ith the smallest distance, from the priorty queue
#         curr_distance, curr_vertex = heapq.heappop(pq)

#         # If current distance is larger than known distance, skip
#         if curr_distance > distances[curr_vertex]:
#             continue

#         # Explore the neighbors of the current vertex
#         for neighbor, weight in graph[curr_vertex].items():
#             distance = distances[curr_vertex] + weight

#             # If this path is shorter than previously known, update the known distance
#             # store the predecessor, and add this to the heap for processing
#             # Note: this potentially adds the same vertex to the heap, to avoid this
#             # consider implementing a heap that allows for updating an existing entry
#             # in the heap
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 predecessors[neighbor] = curr_vertex
#                 heapq.heappush(pq, (distance, neighbor))

#     return distances, predecessors