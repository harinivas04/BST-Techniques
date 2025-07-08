class node:
    def __init__(self,data):
        self.right=None
        self.data=data
        self.left=None
class bst:
    def __init__(self):
        self.root=None
    
    def insert(self,root,data):
        if root==None:
            return node(data)
        if root.data>data:
            root.left=self.insert(root.left,data)
        if root.data<data:
            root.right=self.insert(root.right,data)
        return root
        
    def insert_val(self,data):
        self.root=self.insert(self.root,data)
        
    def top_view(self):
        print("Top View:")
        hd_map = {}
        def dfs(node, hd, level):
            if not node:
                return
            if hd not in hd_map or level < hd_map[hd][1]:
                hd_map[hd] = (node.data, level)
            dfs(node.left, hd - 1, level + 1)
            dfs(node.right, hd + 1, level + 1)

        dfs(self.root, 0, 0)
        for hd in sorted(hd_map):
            print(hd_map[hd][0], end=' ')
        print()    
        
    def bottom_view(self):
        print("Bottom View:")
        hd_map = {}

        def dfs(node, hd, level):
            if not node:
                return
            if hd not in hd_map or level >= hd_map[hd][1]:
                hd_map[hd] = (node.data, level)
            dfs(node.left, hd - 1, level + 1)
            dfs(node.right, hd + 1, level + 1)

        dfs(self.root, 0, 0)
        for hd in sorted(hd_map):
            print(hd_map[hd][0], end=' ')
        print()
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    
    def display(self):
        self.inorder(self.root)
        print('None')
        
l=list(map(int,input().split()))
b=bst()
for i in l:
    b.insert_val(i)
b.display()
b.top_view()
b.bottom_view()