 
def nthFibonacci(  n):
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        a=1
        b=1
        sum=0
        for i in range(3,n+1):
            sum=(a +b )  
            a=b
            b=sum
        return sum
print(nthFibonacci(4))