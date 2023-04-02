n=5
arr=[1,2,3,4,5]
x=3
def check(arr,n,x):
    if arr[n]==x:
        return True
    elif n==1:
        return False
    else:
        return check(arr,n-1,x)