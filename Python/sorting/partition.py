# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    left = 0
    right = len(arr) - 1
    pivot_index = left
    pivot = arr[left]
    left += 1
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    temp = arr[right]
    arr[right] = arr[pivot_index]
    arr[pivot_index] = temp
    return arr