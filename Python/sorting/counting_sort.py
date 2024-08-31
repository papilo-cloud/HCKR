# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    temp_arr = []
    for j in range(len(arr)//2):
        arr[j][1] = '-'
    arr.sort(key= lambda x: int(x[0]))
    for i in arr:
        temp_arr.append(i[1])

    print(*temp_arr)