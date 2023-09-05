import random

def get_numbers():
    a = []
    with open('./quicksort_array.txt') as f:
        for line in f:
            data = line.split()
            a.append(int(data[0]))
    return a


def find_median(a, low, high):
        first = a[low]
        last = a[high]
        if len(a) % 2 == 0:
            middle_index = ((high - low) // 2) - 1
        else:
            middle_index = ((high - low) // 2)
        middle = a[middle_index]
        
        minval = min([first, middle, last])
        maxval = max([first, middle, last])
        if first != minval and first != maxval:
            return low
        elif middle != minval and middle != maxval:
            return middle_index
        else:
            return (high)


def choose_pivot(a, pivot_type, low, high):
    if pivot_type == 'first':
        return low
    elif pivot_type == 'last':
        return high
    elif pivot_type == 'median':
        return(find_median(a, low, high))
    elif pivot_type == 'random':
        return random.randint(low, high)
    else:
        raise AssertionError('pivot_type must be one of ["first", "last", "median"]')
    

def partition(a, pivot_type,  low, high):
    pivot_idx = choose_pivot(a, pivot_type, low, high)

    # move the pivot to the zero index
    a[low], a[pivot_idx] = a[pivot_idx], a[low]

    # Partition the array into two halves
    i = low
    for j in range(low, high):
        if a[j + 1] < a[low]:
            a[i + 1], a[j + 1] = a[j + 1], a[i + 1]
            i += 1

    # Move the pivot to the index between the two halves
    a[low], a[i] = a[i], a[low]
    
    return i


def quicksort(a, pivot_type, low, high):
    comparisons = 0
    if low >= high:
        return comparisons
    
    pivot_idx = partition(a, pivot_type, low, high)

    # Make recursive calls with left and right partition,
    # excluding the pivot index
    comparisons = high - low
    l_comp = quicksort(a, pivot_type, low, pivot_idx - 1)
    r_comp = quicksort(a, pivot_type, pivot_idx + 1, high)
    comparisons += l_comp + r_comp

    return comparisons


if __name__ == "__main__":
    # a = [9, 3, 7, 5, 6, 4, 8, 2, 1]
    a = get_numbers()

    comparisons = quicksort(a,'first', 0, len(a) - 1)
    print(comparisons)
    a = get_numbers()
    comparisons = quicksort(a, 'last', 0, len(a) - 1)
    print(comparisons)
    a = get_numbers()
    comparisons = quicksort(a, 'median', 0, len(a) - 1)
    print(comparisons)
    # print(a)