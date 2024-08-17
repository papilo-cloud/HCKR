# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    res = []
    for i in queries:
        count = 0
        for j in stringList:
            if i == j:
                count += 1
        res.append(count)
    return res