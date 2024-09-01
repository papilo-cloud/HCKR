# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here

    left_sum = 0
    right_sum = sum(arr[1:])
    i = 1
    while i < len(arr):

        if left_sum == right_sum:
            return 'YES'
        else:
            left_sum += arr[i - 1]
            right_sum -= arr[i]
        i += 1
    if left_sum == right_sum:
        return 'YES'
    return 'NO'