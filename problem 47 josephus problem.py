n=3
k=2
#for 0 based indexing 
def josephus(n,k):
    if n==1:
        return 0 
    return (josephus(n-1,k) +k)%n 




# for 1 based indexing 

        
def jos(n,k):
        if n==1:
            return 0
        return ( jos(n-1,k) +k)%(n ) 
def josephus(n,k):
        return   jos(n,k) +1
print(josephus(n,k)  )

    
    
    
    