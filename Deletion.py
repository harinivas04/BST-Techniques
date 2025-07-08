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
        if root.data<data:
            root.right=self.insert(root.right,data)
        if root.data>data:
            root.left=self.insert(root.left,data)
        return root
    
    def insert_val(self,data):
        self.root=self.insert(self.root,data)
        
    def dele(self,root,data):
        if root==None:
            return None
        if root.data>data:
            root.left=self.dele(root.left,data)
        elif root.data<data:
            root.right=self.dele(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp=suc(root.right)
            root.data=temp.data
            root.right=self.dele(root.right,temp.data)
        return root
    
    def dele_val(self,data):
        self.root=self.dele(self.root,data)
            
    def suc(slef,node):
        cur=node
        while cur.left is not None:
            cur=cur.left
        return cur
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end='->')
            self.inorder(root.right)
            
    def display(self):
        self.inorder(self.root)
        print('None')
        
l=list(map(int,input().split()))
b=bst()
for i in l:
    b.insert_val(i)
b.display()
b.dele_val(84)
b.display()