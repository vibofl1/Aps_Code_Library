 

class Solution:
    def sumOfMatrix(self,n,m,arr):
         
        ans=[]
        su=0
        for i in range(n):
            for j in range(m):
                
                su = su+ arr[i][j]
                # print(su)
             
        # print(ans)
        return su
                
                
            
            


 

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(' '))
        Grid = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(M):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.sumOfMatrix(N,M,Grid)) 
 