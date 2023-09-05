def merge(a, b):
    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if(a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    
    return c

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    b = mergesort(a[0:mid])
    c = mergesort(a[mid:len(a)])
    a = merge(b, c)

    return a


if __name__ == "__main__":
    a = [9, 3, 7, 5, 6, 4, 8, 2, 1]
    print(mergesort(a))