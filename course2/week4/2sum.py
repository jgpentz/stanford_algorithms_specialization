import os
from tqdm import tqdm

def get_data():
    with open(f'{str(os.getcwd())}/course2/week4/2sum.txt') as f:
        data = [int(line.split()[0]) for line in f]
    return data


def two_sum(data, interval):
    sum = 0
    values = set()
    
    # Insert numbers into hash table in constant time (O(n))
    for val in data:
        values.add(val)
    
    # Look up distinct x + y = t target values in constant time (O(n))
    for t in tqdm(range(interval[0], interval[1] + 1)):
        for x in values:
            if (t - x) in values:
                sum += 1
                break

    print(sum)



if __name__ == "__main__":
    data = get_data()
    # interval = [3, 10]
    interval = [-10000, 10000]
    two_sum(data, interval)