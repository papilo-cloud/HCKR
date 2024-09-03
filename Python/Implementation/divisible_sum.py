# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(1+i, n):
            if (ar[i] + ar[j])%k == 0:
                count += 1
    return count