import sys
sys.setrecursionlimit(2 ** 20)

def read_data():
    '''
    Reads in value and their weights

    Returns:
        - Capacity of the knapsack
        - List of tuples of the item value and weight e.g. (10, 100) corresponds
        to value 10 with a weight of 100
    '''
    items  = []
    values = []
    weights = []
    capacity = 0
 
    with open('knapsack_big.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                capacity = int(line.strip().split(' ')[0])
                continue
            value, weight = line.strip().split(' ')
            values.append(int(value))
            weights.append(int(weight))
    return capacity, values, weights


def find_knapsack(capacity, weights, values, n):
    dp = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    return find_knapsack_value(capacity, weights, values, n, dp)


def find_knapsack_value(capacity, weights, values, n, dp):
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    #If we have solved it earlier, then return the result from memory
    if dp[n][capacity] != -1:
        return dp[n][capacity]
 
    #Otherwise, we solve it for the new combination and save the results in the memory
    if weights[n-1] <= capacity:
        dp[n][capacity] = max(
            values[n-1] + find_knapsack_value(capacity-weights[n-1], weights, values, n-1, dp),
            find_knapsack_value(capacity, weights, values, n-1, dp)
            )
        return dp[n][capacity]

    dp[n][capacity] = find_knapsack_value(capacity, weights, values, n-1, dp)
    return dp[n][capacity] 


if __name__ == "__main__":
    capacity, values, weights = read_data()
    print(find_knapsack(capacity, weights, values, len(values)))
