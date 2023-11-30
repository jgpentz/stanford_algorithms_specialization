import os


def read_data():
    '''
    Reads in symbols (line numbers) and their weights (frequency)

    Returns:
        List of tuples of the weight and symbol e.g. (104, 0) corresponds
        to symbol 0 with a weight of 104
    '''
    nodes = []

    with open(f'{str(os.getcwd())}/course3/week3/mwis.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            node = ''.join(line.strip().split(' '))
            nodes.append(int(node))

    return nodes


def mwis(path):
    mwis = [0] * (len(path) + 1)
    mwis[0] = 0
    mwis[1] = path[0]

    for i in range(2, len(path) + 1):
        mwis[i] = max(mwis[i - 1], mwis[i - 2] + path[i - 1])

    s = []
    i = len(path)

    while i > 0:
        if mwis[i] > mwis[i - 2] + path[i - 1]:
            i -= 1
            s.append(i)
        else:
            s.append(i)
            i -= 2

    return mwis[len(path)], s

if __name__ == "__main__":
    a = read_data()
    
    _, mwis_nodes = mwis(a)
    
    candidates = [1, 2, 3, 4, 17, 117, 517, 997]
    s = ['1' if candidate in mwis_nodes else '0' for candidate in candidates]
    print(''.join(s))
