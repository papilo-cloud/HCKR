# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    shifts = 0
    n = len(arr)
    
    for i in range(1, n):
        pos = i
        tem_val = arr[i]
        
        while pos > 0:
            if arr[pos - 1] > tem_val:
                arr[pos] = arr[pos - 1]
                shifts += 1
                pos -= 1
            else:
                break
        arr[pos] = tem_val
    return shifts