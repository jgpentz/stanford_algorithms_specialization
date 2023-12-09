def bellman_ford(g, s, num_vertices):
    distance = [float('inf')] * num_vertices
    predecessors = [-1] * num_vertices
    distance[s] = 0

    # Relax edges |V| - 1 times or until convergence
    for _ in range(num_vertices - 1):
        stable = True

        for u, v, w in g:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessors[v] = u
                stable = False

        if stable:
            break

    # Check for negative cycles
    for u, v, w in g:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            raise ValueError('Graph contains negative cycle ')

    return distance, predecessors

if __name__ == "__main__":
    # Example usage:
    g = []
    g.append((0, 1, -1))
    g.append((0, 2, 4))
    g.append((1, 2, 3))
    g.append((1, 3, 2))
    g.append((1, 4, 2))
    g.append((3, 2, 5))
    g.append((3, 1, 1))
    g.append((4, 3, -3))

    source_vertex = 0
    distances, predecessors = bellman_ford(g, source_vertex, 5)
    
    print("Shortest distances from source vertex {}:".format(source_vertex))
    for i in range(len(distances)):
        print("Vertex {}: Distance: {}, Predecessor: {}".format(i, distances[i], predecessors[i]))
