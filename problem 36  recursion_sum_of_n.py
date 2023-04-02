n=int(input())
def sum_n(n):
    if n==0:
        return 0 
    smalloutput= sum_n(n-1)
    return  n + smalloutput 
    
print(sum_n(n))