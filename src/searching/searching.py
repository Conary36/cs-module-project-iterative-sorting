def linear_search(arr, target):
    # Your code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
# def binary_search(arr, target):
#
#     # Your code here
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        my_choice = arr[middle]
        if my_choice == target:
            return middle
        if my_choice > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
