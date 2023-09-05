import random

def partition(a, low, high):
    pivot = random.randint(low, high)

    # Swap pivot to zero index
    a[low], a[pivot] = a[pivot], a[low]

    # Partition into left and right halves
    # note: Can update a[j + 1] < a[low] comparison to be
    #  a[j + 1] > a[low] to make this algo find the
    # kth largest element
    i = low
    for j in range(low, high):
        if a[j + 1] < a[low]:
            a[i + 1], a[j + 1] = a[j + 1], a[i + 1]
            i += 1
        
    # Move pivot to the index between the partitioned halves
    a[low], a[i] = a[i], a[low]

    return i


def quickselect(a, k, low, high):
    if low == high:
        return a[low]
    
    pivot_idx = partition(a, low, high)

    if pivot_idx + 1 == k:
        return a[pivot_idx]
    elif pivot_idx + 1 > k:
        return quickselect(a, k, low, pivot_idx - 1)
    else:
        return quickselect(a, k, pivot_idx + 1, high)

if __name__ == "__main__":
    a = [9, 3, 7, 5, 6, 4, 8, 2, 1, 10]
    # Note: to find kth largest, pass len(a) + 1 - kth
    for kth in range(1, (len(a) + 1)):
        print(quickselect(a, kth, 0, len(a) - 1)) 