class node:
    def __init__(self,data):
        self.data=data
        self.right=None
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
        
    def left_view(self):
        print("Left View:")
        result = []
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.data)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(self.root, 0)
        print(*result)

    def right_view(self):
        print("Right View:")
        result = []
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.data)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(self.root, 0)
        print(*result)
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    
    def display(self):
        self.inorder(self.root)
        print('None')
b=bst()
l=list(map(int,input().split()))
for i in l:
    b.insert_val(i)
b.display()
b.left_view()
b.right_view()