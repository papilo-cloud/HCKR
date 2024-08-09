def getMax(operations):
    # Write your code here
    stack = []
    max_stack = []
    result = []
    
    def push(elem):
        stack.append(elem)
        if len(stack) == 1:
            max_stack.append(elem)
            return
        
        if elem > max_stack[-1]:
            max_stack.append(elem)
        else:
            max_stack.append(max_stack[-1])
    
    def pop():
        stack.pop()
        max_stack.pop()
    
    def print_max():
        result.append(max_stack[-1])
    
    for i in (operations):
        arr = int(i[0])
        
        if arr == 1:
            push(int(i[2:]))
        if arr == 2:
            pop()
        if arr == 3:
            print_max()
    return result