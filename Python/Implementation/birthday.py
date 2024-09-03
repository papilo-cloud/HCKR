# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    n = len(s)
    if m > n:
        return 0
    window = sum(s[:m])
    count = 0
    if window == d:
        count += 1
    
    for i in range(n - m):
        window = window - s[i] + s[i + m]
        if window == d:
            count += 1
    return count