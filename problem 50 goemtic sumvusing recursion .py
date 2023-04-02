


def gos(k):
    if k==0:
        return 1 
    return  gos(k-1) +(1/(2**k))
print(gos(5))