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
        
    def flca(self,root,n1,n2):
        if root==None:
            return None
        if root.data>n1 and root.data>n2:
            return self.flca(root.left,n1,n2)
        if root.data<n1 and root.data<n2:
            return self.flca(root.right,n1,n2)
        return root
        
    def dis(self,root,data):
        di=0
        while root.data!=data:
            if data<root.data:
                root=root.left
            else:
                root=root.right
            di+=1
        return di
        
    def dis_t(self,n1,n2):
        ans=self.flca(self.root,n1,n2)
        return self.dis(ans,n1)+self.dis(ans,n2)
    
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
print(f'{b.dis_t(5,12)}')
