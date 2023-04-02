
class Node:
    def __init__(self,key)  :
        self.key=key
        self.left=None
        self.right=None 
 
      
#recursive approach 


def insert(root, key):
    
    if root==None:
        return Node(key)
    elif root.key==key:
        return root
    elif root.key > key :
        root.left=  insert(root.left,key)
    else:
        root.right= insert(root.right,key)
    return root

#iterative approach 
def insert(root, key):
     
    par=None
    cur=root
    while cur!=None :
        par=cur
        if cur.key==key:
             return root
        if cur.key>key :
            cur=cur.left
        else:
            cur=cur.right
    if root==None:
        return Node(key)    
    if par .key >  key :
        par.left= Node(key )
    else :
        par.right=Node(key )
        
    return    root
arr=[1,2,3,4,5,10,30,60] 
root=Node(100)
for x in arr: 
    insert(root,x) 
def postorder ( root):
        if root!=None:
            postorder(root.left)
            postorder(root.right)       
            print(root.key) 
postorder(root)
    