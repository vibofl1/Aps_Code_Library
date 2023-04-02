m=3
n=5
def mul(m,n):
    if n==0:
        return 0
    return mul(m,n-1) + m 
print(mul(m,n))