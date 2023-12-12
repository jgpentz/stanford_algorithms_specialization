
from math import sqrt

def read_data():
    '''
    Reads in cities and their x, y coordinates

    Returns:
        list of cities identified by a tuple of their x, y coordinates
    '''
    cities = []

    with open('nn.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            _, x, y  = line.strip().split(' ')
            cities.append((float(x), float(y)))

    return cities


def get_distance(a, b):
    '''
    Calculates the euclidean distance between a pair of points (a1,  b1), (a2, b2)
    '''
    dist = sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

    return dist


def tsp_heuristic(cities):
    total_dist = 0
    visited = set()
    visited.add(cities[0])
    current_city = cities[0]
    for i in range(len(cities) - 1):
        shortest = (None, float('inf'))
        for city in cities:
            if city not in visited:
                dist = get_distance(current_city, city)
                if dist < shortest[1]:
                    shortest = (city, dist)

        visited.add(shortest[0])
        current_city = shortest[0]
        total_dist += shortest[1]

    total_dist += get_distance(current_city, cities[0])    

    return int(total_dist)


if __name__ == "__main__":
    cities = read_data()
    print(tsp_heuristic(cities))
