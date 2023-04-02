n=5
arr=[1,2,3,4,5]

def  issorted(arr):
    l=len(arr)
    if l==0 or l==1:
        return True
    if arr[0]>arr[1]:
        return False
    smallerlist=arr[1:]
    issmallerlist=issorted(smallerlist)
    return issmallerlist
print(issorted(arr))   
 


#better approach
def issorted_b(arr,si):
        l=len(arr)
        if si==l-1 or si==l:
            return True
        if arr[si]>arr[si+1]:
            return False 
        issl=issorted_b(arr,si+1)
        return issl
print(issorted_b(arr,0))  
        
            
    
    
      