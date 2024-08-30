#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    freq = [0 for x in range(100)]
    
    for j in arr:
        freq[j] += 1
    return freq