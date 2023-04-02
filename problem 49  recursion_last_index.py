arr=[1,2,9,3,4,9,85,7,4,32]
print(arr.index(4,5,9))
x=4
n=len(arr)
def lid(arr,x):
    l=len(arr)
    if l==0:
        return -1 
    smallerlist=arr[1:]
    id=lid(smallerlist,x) 
     
    if id !=-1 :
        return id +1
        
    else: 
        if arr[0]==x:
            return 0
        else: 
            return -1 
     
print(lid(arr,x))
si=0
def lid_b(x,si):
    l=len(arr)
    if si==l:
        return -1
    id=lid_b(x,si+1)
    # return id 
    if id !=-1 :
        return id 
    else: 
        if arr[si]==x:
            print(si)
            return si 

    
        else:
            return -1 
        
print(lid_b(x,si+1))
    
     
    