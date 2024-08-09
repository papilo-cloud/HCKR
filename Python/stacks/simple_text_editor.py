# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:
    def __init__(self):
        self.str = ''
        self.undoprev = []
        self.data = []
    
    
    def append(self, elem):
        self.str = self.str + elem
        self.data.append(elem)
        self.undoprev.append('WRITE')
        

    def undo(self):
        
        if len(self.undoprev) > 1:
            if self.undoprev[-1] == 'WRITE':
                self.str = self.str[: -len(self.data.pop())]
                self.undoprev.pop()
            elif self.undoprev[-1] == 'DELETE':
                self.str += self.data.pop()
                self.undoprev.pop()
            
        elif len(self.undoprev) == 1:
            if self.undoprev[0] == 'WRITE':
                self.str = self.str[: -len(self.data.pop())]


    def delete_last_nth_elem(self, n):
        start = self.str[:-n]
        end = self.str[-n:]
        
        self.str = start
        self.data.append(end)
        self.undoprev.append('DELETE')
            
    
    def print_n_elem(self, n):
        return self.str[n - 1]
    
    def to_string(self):
        return self.str
        
        
stack = Stack()


q = int(input())

for i in range(q):
    operations = input().split()
    
    if operations[0] == '1':
        stack.append(operations[1])
    elif operations[0] == '2':
        stack.delete_last_nth_elem(int(operations[1]))
    elif operations[0] == '3':
        print(stack.print_n_elem(int(operations[1])))
    else:
        stack.undo()