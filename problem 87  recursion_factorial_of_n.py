n=int(input())
def fact(n):
    if n==0:
        return 1 
    smalloutput=fact(n-1)
    return n * smalloutput 
print(fact(n))