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
    step = 1

    while step < len(a):
        tmp = []
        for i in range(0, len(a), step * 2):
            tmp.append(merge(a[i:(i + step)], a[i + step : i + step * 2]))
        a = []
        for subarray in tmp:
            for i in subarray:
                a.append(i)

        step = step * 2
        
    return(a)

def mergesort2(a):
    prev = [[n] for n in a]

    while(len(prev) > 1):
        cur = []
        for i in range(0, len(prev), 2):
            cur.append(merge(prev[i], prev[i + 1]) if i + 1 < len(prev) else prev[i])
        print(prev)
        prev = cur

    return(prev[0]) 

if __name__ == "__main__":
    a = [9, 3, 7, 5, 6, 4, 8, 2, 1]
    print(mergesort(a))
    # print(mergesort2(a))