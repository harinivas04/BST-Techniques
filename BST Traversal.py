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
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
            
    def preorder(self,root):
        if root:
            print(root.data,end="->")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="->")
            
    def displays(self):
        self.inorder(self.root)
        print('None')
    
    def display(self):
        self.preorder(self.root)
        print('None')
        
    def displayed(self):
        self.postorder(self.root)
        print('None')
        
l=list(map(int,input().split()))
b=bst()
for i in l:
    b.insert_val(i)
print('Inorder traversal')
b.displays()
print('Preorder traversal')
b.display()
print('postorder Traversal')
b.displayed()
