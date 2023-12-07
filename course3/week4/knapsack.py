def read_data():
    '''
    Reads in symbols (line numbers) and their weights (frequency)

    Returns:
        List of tuples of the item value and weight e.g. (10, 100) corresponds
        to value 10 with a weight of 100
    '''
    items  = []
    capacity = 0
 
    with open('knapsack1.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                capacity = int(line.strip().split(' ')[0])
                continue
            value, weight = line.strip().split(' ')
            items.append((int(value), int(weight)))

    return capacity, items


def knapsack(capacity, items):
    a = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for c in range(capacity + 1):
            if items[i - 1][1] > c:
                a[i][c] = a[i - 1][c]
            else:
                a[i][c] = max(a[i - 1][c], (a[i - 1][c - items[i - 1][1]] + items[i - 1][0]))

    return a[i][c]

if __name__ == "__main__":
    capacity, items = read_data()
    print(knapsack(capacity, items))
    print('a')

