# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    res = []
    dic = {}
    for i in arr:
        for j in brr:
            if i == j:
                brr.pop(brr.index(i))
                break

    for i in brr:
        if dic.get(i) is None:
            dic[i] = True
            res.append(i)
    return sorted(res)