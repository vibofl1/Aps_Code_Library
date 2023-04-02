 

def floor(  root, x):
        # Code here
        res=-1
        c=0
        while root!=None:
             
            # print(c)
            if root.key==x:
                 
                return root.key
                
            elif root.key>x:
                # print("les",root.key,res)
                root=root.left 
                # print("les",root ,res)
            else:
                 
                res=root.key
                root=root.right 
        return res  
 


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

arr=[1,2,3,4,5,10,20,30]            
root=arrtobst(arr)
print(floor(root,8))
# postorder(root)




