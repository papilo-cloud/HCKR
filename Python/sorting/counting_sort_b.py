#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    m = max(arr)
    res = []
    freq = [0 for i in range(m + 1)]
    for j in arr:
        x = j
        freq[x] += 1

    i = 0
    while i < len(freq):
        j = 0
        if i in arr:
            while j < freq[i]:
                res.append(i)
                j += 1
        i += 1

    return res