# Enter your code here. Read input from STDIN. Print output to STDOUT

class Heap:
    def __init__(self) -> None:
        self.data = []
        self.count = 0
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.data.append(value)
        self.count += 1
        new_node_index = len(self.data) - 1
        self.trickle_up(new_node_index)
            
    def trickle_up(self, index):
        if index > 0 and (
            self.data[index] < self.data[self.parent_index(index)]):
            
            temp = self.data[index]
            self.data[index] = self.data[self.parent_index(index)]
            self.data[self.parent_index(index)] = temp
            self.trickle_up(self.parent_index(index))
    
    def print_minimum(self):
        return self.data[0]
        
    def delete_value(self, node_val):
        
        value =  value = None
        i = 0
        while i < len(self.data):
            if self.data[i] == node_val:
                value = self.data[i]
                break
            i += 1
                
        self.count -= 1
        self.data[i] = self.data[-1]
        self.data.pop(i)
        trickle_node_index = i
        
        while self.has_lesser_child(trickle_node_index):
            lesser_child_index = self.calculate_lesser_child_index(trickle_node_index)
            temp = self.data[trickle_node_index]
            self.data[trickle_node_index] = self.data[lesser_child_index]
            self.data[lesser_child_index] = temp
            trickle_node_index = lesser_child_index
        return value
        
    def has_lesser_child(self, index):
        return ((self.left_child_index(index) < self.count and (
                self.data[self.left_child_index(index)] < self.data[index])) or (
                    self.right_child_index(index) < self.count and (
                        self.data[self.right_child_index(index)] < self.data[index]
                    )
                ))

    def calculate_lesser_child_index(self, index):
        
        if self.right_child_index(index) >= self.count:
            return self.left_child_index(index)
        
        if self.data[self.right_child_index(index)] < self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
        
hp = Heap()

q = int(input())
for _ in range(q):
    v = input()
    if int(v[:1]) == 1:
        hp.insert(int(v[2:]))
    elif int(v[:1]) == 2:
        hp.delete_value(int(v[2:]))
    else:
        print(hp.print_minimum())