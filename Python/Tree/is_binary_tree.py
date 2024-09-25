""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if not root:
        return False
    res = []
    s = []
    while True:
        if root:
            s.append(root)
            root = root.left
        else:
            if not s:
                break
            root = s[-1]
            if res and (res[-1] >= root.data):
                return False
            else:
                res.append(root.data)
            s.pop()
            root = root.right
    return True
                
