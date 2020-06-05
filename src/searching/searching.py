def linear_search(arr, target):
    # loop through the array return the value if found
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1

    # return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # if there are no items in the array we return false for target found
    if len(arr) == 0:
        return -1  # not found

    # variables to hold index values for bisection of binary search
    low = 0
    high = len(arr) - 1

    while low <= high:
        # middle = (low + high)/2 could cause a stack overflow if limited memory to hold this value
        # Alternate implementation will low index(intiatially zero) to value of high minus low
        # first loop will just be high value and /2 will give the index of the middle
        middle = low + (high - low) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1
