def pairs(k, arr):
    # Write your code here
    count = 0
    for i in range(len(arr)):
        plus = arr[i]
        for j in range(len(arr)):
            if plus > arr[j]:
                if plus - arr[j] == k:
                    count += 1
    return count