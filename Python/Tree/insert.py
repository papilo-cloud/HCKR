class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        new_node = Node(val)
        #Enter you code here.
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            parent = None
            
            while True:
                parent = current
                if val > current.info:
                    current = current.right
                    if not current:
                        parent.right = new_node
                        return
                else:
                    current = current.left
                    if not current:
                        parent.left = new_node
                        return
        return self.root
                        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)