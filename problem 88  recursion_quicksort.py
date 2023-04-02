arr=[5,4,0,2,1,6,7,3,8]
print(arr)

def partition(arr,s,e):
    pivot_element=arr[s]
    c=0
    for i in range(s,e+1):
        
        # print(pivot_element, e+1,i,arr[i])
        if arr[i]<pivot_element:
            c+=1 
    
    arr[s+c],arr[s]=arr[s],arr[s+c]
    pivotindex=s +c
    print(arr,pivot_element,s,e,pivotindex)
    i=s
    j=e
    while i<j:
        if arr[i]<pivot_element:
            i+=1
        elif arr[j]>=pivot_element:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1 
    return pivotindex 
 
def quicksort(arr,s,e) :
    if s>=e:
        return 
    i=partition(arr,s,e)
    quicksort(arr,s,i-1)
    quicksort(arr,i+1,e)
s=0
e=len(arr) -1
quicksort(arr,0,len(arr)-1)   
print(arr)
