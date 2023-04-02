arr=[1,2,9,3,4,5]
x=4
n=len(arr)
def fid(arr, x):
    if n==0:
        return -1 
    if arr[0]==x:
        return 0
    smalloutput=arr[1:]
    id=fid(smalloutput ,x)
    if id==-1:
        return -1 
    else:
        return id + 1 

print(fid(arr, x))

si=0
def fid_b(arr,x,si):
    l=len(arr)
    if si==l :
        return -1 
    if arr[si] ==x:
        return si 
    return fid_b(arr,x,si+1) 

print(fid_b(arr,x,si))    
    

