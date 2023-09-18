import random

def partition(a, l, r):
    piv_index = random.randrange(l, r)
    a[l], a[piv_index] = a[piv_index], a[l]

    i = l
    for j in range(l, r):
        if a[j + 1] < a[l]:
            a[i + 1], a[j + 1] = a[j + 1], a[i + 1]
            i += 1

    a[l], a[i] = a[i], a[l]

    return i

def quickselect(a, kth, l, r):
    if l >= r:
        return a[l]
    
    piv_index = partition(a, l, r)

    if piv_index + 1 == kth:
        return a[piv_index]
    elif piv_index + 1 > kth:
        return quickselect(a, kth, l, piv_index - 1)
    else:
        return quickselect(a, kth, piv_index + 1, r)
    

if __name__ == "__main__":
    a = [9, 3, 7, 5, 6, 4, 8, 2, 1, 10]
    # print(mergesort(a))
    # quicksort(a, 0, len(a) - 1)
    # print(a)
    for kth in range(1, (len(a) + 1)):
        print(quickselect(a, kth, 0, len(a) - 1))

# if __name__ == "__main__":
#     # Graph G:
#     # 
#     #         --- A --- C ----- E
#     #       /          / \     /
#     #     S           /   \   /
#     #      \         /     \ /
#     #       ------- B ----- D 
#     # 

#     g = {
#         'S': ['A', 'B'],
#         'A': ['S', 'C'],
#         'B': ['S', 'C', 'D'],
#         'C': ['A', 'B', 'D', 'E'],
#         'D': ['B', 'C', 'E'],
#         'E': ['C', 'D']
#     }

#     bfs(g)
    