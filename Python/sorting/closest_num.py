#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    result = []
    right = len(arr) - 1
    arr.sort()
        
    maxx_short = arr[right] - arr[right - 1]
    while right > 0:
        short = arr[right] - arr[right -1]
        if short < maxx_short:
            maxx_short = short
            result.append(arr[right - 1]) 
            result.append(arr[right]) 
            result.pop(0)
            result.pop(0)
        elif short == maxx_short:
            result.append(arr[right - 1])
            result.append(arr[right])
        right -= 1
    return sorted(result)