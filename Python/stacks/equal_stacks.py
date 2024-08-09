
def equalStacks(h1, h2, h3):
    # Write your code here
    stack1 = sum(h1)
    stack2 = sum(h2)
    stack3 = sum(h3)
    
    
    is_equal = False
    while not is_equal and h1 and h2 and h3:
        if stack1 == stack2 == stack3:
            is_equal = True
            break
        elif stack1 > stack2:
            s = h1.pop(0)
            stack1 -= s 
        
        elif stack3 > stack1:
            s = h3.pop(0)
            stack3 -= s
        elif stack2 > stack3:
            s = h2.pop(0)
            stack2 -= s
        
    if is_equal:
        return (stack1)
    else:
        return 0
            
    
    
    

x = equalStacks([1, 2, 1, 1], [1, 1, 2], [1,1])
print(x)
