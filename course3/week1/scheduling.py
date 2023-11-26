import os
def read_data():
    '''
    Reads in the jobs and computes an array for the differences, and 
    another for the ratios.  The computation is done here so that it
    does not need to be repeatedly done in the merge step.

    Returns:
        diff_jobs = [(difference, weight, length)]
        ratio_jobs = [(ratio, weight, length)]
    '''
    diff_jobs = []
    ratio_jobs = []
    with open(f'{str(os.getcwd())}/course3/week1/scheduling_data.txt') as f:
        for line in f:
            weight, length = line.strip().split(' ')
            weight, length = int(weight), int(length)
            diff_jobs.append(((weight - length), weight, length))
            ratio_jobs.append(((weight/length), weight, length))

    return diff_jobs, ratio_jobs


def merge(l, r):
    '''
    Merge two arrays in decreasing order.  When jobs have the same value,
    this will put the job with the higher weight first.
    '''
    i = 0
    j = 0
    c = []

    # Merge until either or both of the arrays have no more values left
    while i != len(l) and j != len(r):
        # In the case that two values are equal, schedule the job with the
        # higher weight first 
        if l[i][0] == r[j][0]:
            if l[i][1] > r[j][1]:
                c.append(l[i])
                i += 1
            else:
                c.append(r[j])
                j += 1
        elif l[i][0] > r[j][0]:
            c.append(l[i])
            i += 1
        else:
            c.append(r[j])
            j += 1
    
    # Tack on any remaining data
    c += l[i:]
    c += r[j:]

    return c
            


def merge_sort(jobs):
    '''Recursively merges the jobs in decreasing order.'''
    # Base case: 1 or fewer elements in an array is sorted by default
    if len(jobs) <= 1:
        return jobs
    
    # Sort the jobs into a left/right half, then merge them
    mid = len(jobs) // 2
    l = merge_sort(jobs[:mid])
    r = merge_sort(jobs[mid:])
    merged_jobs = merge(l, r)

    return merged_jobs


def calulate_completion_times(jobs):
    '''
    Sorts the jobs in decreasing order of their difference score, and then
    computes the sum of weighted completion times.

    Time complexity:
        - Reading in the data: O(n)
        - Sorting the array: O(n log n)
        - Computing the completion times: O(n)

        Total dominated by sorting step: O(n log n)

    Space complexity:
        - Reading data: O(n)
        - Sorting the array: O(n)
        - Computing completion times: O(1)

        Total: O(n)
    '''
    # Use merge sort to sort by weighted difference
    sorted_jobs = merge_sort(jobs)

    # Sum the completion times
    sum = 0
    completion_time = 0
    for i in range(len(sorted_jobs)):
        # sum = weight[i] * completion_time[i], where completion time is
        # length[0] + length[1] + ... + length[n]
        completion_time += sorted_jobs[i][2]
        sum += sorted_jobs[i][1] * completion_time

    return sum


if __name__ == "__main__":
    diff_jobs, ratio_jobs = read_data()
    
    diff_sum = calulate_completion_times(diff_jobs)
    print(f"Differece sum: {diff_sum}")

    ratio_sum = calulate_completion_times(ratio_jobs)
    print(f"Ratio sum: {ratio_sum}")