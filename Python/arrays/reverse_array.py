# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    i = 0
    j = len(a) - 1
    while i < len(a)//2:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
    return a