class Node:
    def __init__(self,key)  :
        self.key=key
        self.left=None
        self.right=None
        
def ceil (root,x):
    if root==None:
        return  
    if root.key==x:
        return root  
    if root.key < x :
        ceil(root.right,x ) 
    else:
        res=res.append()
        ceil(root.left,x)
     
 
class Node:
    def __init__(self,key)  :
        self.key=key
        self.left=None
        self.right=None
        
def arrtobst(arr):
    n=len(arr)
    if arr is None or n<=0:
        return None  
    
    mid=(n-1)//2
    root=Node(arr[mid])
    root.left=arrtobst(arr[:mid])
    root.right=arrtobst(arr[mid+1:])
    return root

    
    
 

arr=[1,2,3,4,5,10,20,30]            
root=arrtobst(arr)       
 
print(ceil (root,8)         )  
 