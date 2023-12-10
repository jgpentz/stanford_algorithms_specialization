from itertools import combinations
from math import sqrt

def read_data():
    '''
    Reads in cities and their x, y coordinates

    Returns:
        list of cities identified by a tuple of their x, y coordinates
    '''
    cities = []

    with open('tsp.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            x, y  = line.strip().split(' ')
            cities.append((float(x), float(y)))

    return cities


def get_distance(a, b):
    '''
    Calculates the euclidean distance between a pair of points (a1,  b1), (a2, b2)
    '''
    dist = sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

    return dist


def tsp(cities):
    '''
    Find the shortest tour distance using dynamic programming
    in O(n^2 * 2^n) time
    '''
    subsets = {}
    i = 0

    # Store all of the combinations of paths 
    for k in range(len(cities) + 1):
        for subset in combinations(range(2, len(cities) + 1), k):
            subsets[(1,) + subset] = k + 1
            i += 1
    
    # Initialize the base case all subsets with destination of start (1)
    # Set all subsets (except s {1}) to +inf to avoid visiting vertex 1 twice
    a = {}
    for subset in subsets:
        a[(subset, 1)] = 0 if len(subset) == 1 else float('inf')

 
    for m in range(2, len(cities) + 1):
        for subset, l in subsets.items():
            # Only compute values for subsets of size m that contains 1
            if l != m:
                continue

            for j in subset[1:]:
                distances = []
                leftovers = tuple(x for x in subset if x != j)
                for k in subset:
                    if k != j:
                        distances.append(a[(leftovers, k)] + 
                                         get_distance(cities[k - 1], cities[j - 1]))

                a[(subset, j)] = min(distances)

    # Compute the shortest total path distance
    candidates = []
    all_vertices = tuple(range(1, len(cities) + 1))
    for j in range(2, len(cities) + 1):
        candidates.append(a[(all_vertices, j)] + get_distance(cities[j - 1], cities[0]))

    return min(candidates)


if __name__ == "__main__":
    cities = read_data()
    # heuristic approach
    # https://www.coursera.org/learn/algorithms-npcomplete/discussions/weeks/2/threads/FNo8tpFPEeeH2hLapWklpg
    # divide the cities into two parts, cities[0:13] and cities[11:25]
    # compute the shortest tour distance first then subtract twice of distance of cities 12 and 13
    min_1 = tsp(cities[:13])
    min_2 = tsp(cities[11:])
    total_dist = min_1 + min_2 - (2 * get_distance(cities[11], cities[12]))
    print(int(total_dist))
