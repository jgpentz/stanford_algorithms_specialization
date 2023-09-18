import os
import heapq

def get_data():
    data = []
    with open(f'{str(os.getcwd())}/course2/week3/test_data.txt') as f:
            data = [int(line.split()[0]) for line in f]
    return(data)


def find_medians(data):
    # implemented with max heap
    low_heap = []
    # implemented with min heap
    high_heap = []
    # running sum of meadians
    sum = 0

    for i in range(len(data)):
        # Check if this should be added to low heap or high heap
        # Note: using negative sign for max heap (built in python
        # implementation is a min heap)
        if len(low_heap) == 0:
            heapq.heappush(low_heap, -data[i])
        else:
            if data[i] > -low_heap[0]:
                heapq.heappush(high_heap, data[i])
            else:
                heapq.heappush(low_heap, -data[i])

            # Rebalance the heap
            if len(low_heap) > (len(high_heap) + 1):
                heapq.heappush(high_heap, -heapq.heappop(low_heap))
            elif len(high_heap) > len(low_heap):
                heapq.heappush(low_heap, -heapq.heappop(high_heap))

        # Get median
        median = -low_heap[0]
        print(f'low: {low_heap}, high: {high_heap}, median: {median}')

        # Calculate the running sum %10000
        sum += median
          
    return sum % 10000

if __name__ == "__main__":
    data = get_data()
    sum = find_medians(data)

    print(sum)