# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    max_area = 0
    stack = []
    length = len(h)
    i = 0
    
    while i <= length:
        if i == length:
            height = 0
        else:
            height = h[i]
        if (not stack) or (height >= h[stack[-1]]):
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            max_area = max(max_area, h[top] * ((i - stack[-1] -1) if stack else i))
    return max_area