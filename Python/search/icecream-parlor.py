def icecreamParlor(m, arr):
    # Write your code here
    for i in range( len(arr)):
        if arr[i] < m:    
            for x in range(1, len(arr)):
                if (i != x) and arr[i] + arr[x] == m:
                    return [i+1, x+1]
                
ar = [1, 4, 5, 3, 2]
print(icecreamParlor(4, ar))