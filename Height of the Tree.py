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
        
    def height(self,root):
        if root is None:
            return 0
        return 1+max(self.height(root.right),self.height(root.left))
    
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
print(b.height(b.root))