
def get_numbers():
    a = []
    with open('./inversions.txt') as f:
        for line in f:
            data = line.split()
            a.append(int(data[0]))

    return(a)

def merge(a, b):
    i = 0
    j = 0
    c = []
    num_inversions = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            num_inversions += (len(a) - i)

    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    
    return c, num_inversions

def count_inversions(a):
    l = 1
    h = len(a)
    inv_count = 0
    if l < h:
        mid = (l + h) // 2
        b, bi = count_inversions(a[:mid])
        c, ci = count_inversions(a[mid:])
        a, ai = merge(b, c)

        inv_count = ai + bi + ci
    
    return a, inv_count

def mergeSortInversions(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        c = []

        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)

        i = 0
        j = 0
        inversions = 0 + ai + bi

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                inversions += (len(a) - i)
        c += a[i:]
        c += b[j:]

    return c, inversions


if __name__ == "__main__":
    a = get_numbers()
    sorted_nums, inversions = count_inversions(a)
    # print(sorted_nums)
    print(inversions)
    c, inversions = mergeSortInversions(a)
    print(inversions)