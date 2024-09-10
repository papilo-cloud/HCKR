from heapq import heappop, heappush
#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
def runningMedian(a):
    # Write your code here
    heapA = []
    heapB = []
    res = []
    for i in a:
        heappush(heapA, -i)
        heappush(heapB, -heappop(heapA))
        if len(heapB) > len(heapA):
            heappush(heapA, -heappop(heapB))
        
        if len(heapB) != len(heapA):
            res.append(-heapA[0]/1)
        else:
            res.append((heapB[0] - heapA[0])/2)
    return res