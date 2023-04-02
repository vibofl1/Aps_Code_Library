arr=[1,2,3,4,5,6,7]


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

    
    
def postorder ( root):
        if root!=None:
            postorder(root.left)
            postorder(root.right)       
            print(root.key) 
            
root=arrtobst(arr)
postorder(root)




