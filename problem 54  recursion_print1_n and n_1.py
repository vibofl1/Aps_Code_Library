n=int(input())
def print1_n(n):
    if n==0:
        return 
    print1_n(n-1)
    print(n)
    # return 
 
 
#printing from n to 1  
def print_n_1(n)  :
    if n==0:
        return 
    print(n) 
    print_n_1(n-1)

print(print1_n(n))
print(print_n_1(n))

