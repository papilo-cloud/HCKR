# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        temp_val = i
        val = arr[i]
        while temp_val > 0:
            if arr[temp_val - 1] > val:
                arr[temp_val] = arr[temp_val - 1]
                temp_val -= 1
            else:
                break
        arr[temp_val] = val
        print(*arr)