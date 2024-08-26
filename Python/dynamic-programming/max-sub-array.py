# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    max_subsequence = 0
    max_subarray = 0
    sub_array = 0
    
    for i in range(len(arr)):
        
        if len(arr) == 1:
            max_subarray = arr[i]
            max_subsequence = arr[i]
        else:
            if sub_array + arr[i] < 0:
                sub_array
            else:
                sub_array += arr[i]

            if sub_array < 0:
                sub_array = 0
            
            if arr[i] > 0:
                max_subsequence += arr[i]

            if sub_array > max_subarray:
                max_subarray = sub_array
            if sub_array == 0:
                max_subarray = -1
            if i == len(arr)-1 and max_subsequence == 0:
                max_subsequence = -1
    return [max_subarray, max_subsequence]