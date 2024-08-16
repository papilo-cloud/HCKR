def hourglassSum(arr):
    # Write your code here
    hour_glass = -100
    for i in range(4):
        for j in range(4):
            a = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            b = arr[i+1][j+1]
            c = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum = a+b+c
            if sum > hour_glass:
                hour_glass = sum
    return hour_glass