# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    x = len(arr) - 1
    for i in range(d):
        st = arr[0]
        for j in range(x):
            arr[j] = arr[j + 1]
        arr[x] = st
    return arr