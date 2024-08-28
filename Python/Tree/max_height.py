# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
    res = max_height(root)
    return res - 1
    
def max_height(root):
    if not root:
        return 0
    else:
        left_h = max_height(root.left)
        right_h = max_height(root.right)
    
    return max(left_h, right_h) + 1