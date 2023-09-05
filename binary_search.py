def binary_search(a, val):
    if len(a) == 1 and a[0] != val:
        return False
    
    mid = len(a) // 2
    if a[mid] == val:
        return mid
    elif a[mid] > val:
        return binary_search(a[:mid], val)
    else:
        index = binary_search(a[mid:], val)
        if index != False:
            index += mid
        return index


if __name__ == "__main__":
    a = [9, 3, 7, 5, 6, 4, 8, 2, 1]
    a.sort()
    for i in range(0, 12):
        print(binary_search(a, i))