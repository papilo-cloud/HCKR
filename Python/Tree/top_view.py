def top_view(self, root):
        if not root:
            return
        
        queue = []
        hash_table = {}
        hd = 0 # horizontal distance.
        root.hd = hd
        queue.append(root)
        
        while queue:
            root = queue[0]
            hd = root.hd
            
            if hd not in hash_table:
                hash_table[hd] = root.data 
            if root.left:
                root.left.hd = hd - 1
                queue.append(root.left)
            if root.right:
                root.right.hd = hd + 1
                queue.append(root.right)
            queue.pop(0)
        for i in sorted(hash_table):
            print(hash_table[i], end=' ')