# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  # set default  value of index for comparison with smallest_index
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # starts from current index to end of array
        for j in range(i + 1, len(arr)):
            # from elements above current element if value above is less than current index
            # set the current index of smallest index equal to that index value
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # perform swap assignment of values at these two indexes using swap syntax
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    swapped = True
    while swapped:
    '''This swapped above will only = false will and break the loop once the
       if statement where left value is not greater than the right value is not true
       and will then make statement false and break the loop'''
     swapped = False
      for i in range(0, len(arr) - 1):
           if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
            swapped = True
    return arr


"""
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    counts = [0] * (maximum + 1)

    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[value] += 1
    
    j = 0
    for i in range(0, len(counts)):
        while counts[i] > 0:
            arr[j] = i
            j += 1
            counts[i] -= 1

    return arr


def counting_sort2(arr, maximum=None):
    if len(arr) == 0:
        return arr

    if maximum is None:
        maximum = max(arr)

    buckets = [0] * (maximum+1)
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            buckets[value] += 1

    # reinsert values into original array using counts
    j = 0
    for i in range(0, len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
    return arr
