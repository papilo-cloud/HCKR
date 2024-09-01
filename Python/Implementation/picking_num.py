def picking_numbers(arr):
    arr.sort()
    right = 0
    left = 0
    count = 0
    while right < len(arr):
        if abs(arr[left] - arr[right]) >1:
            left += 1
        else:
            count = max(count, (right - left)+1)
            right += 1
    return count
x = [4,6,5,3,3,1]

print(picking_numbers(x))