#User function Template for python3

class Solution:
	def Mutliply(self, matrixA ,matrixB):
		n=len(matrixA[0])
		ans=[]
		
		for i in range(n):
		    l=[]
		    for j in range(n):
		        su=0
		        for k in range (n):
		            mu=matrixA[i][k]*matrixB[k][j]
		            su+=mu
		          #  print(su)
		        l.append(su)
		      #  print(l)
	        ans.append(l)
		  #  print(ans)
		for i in range(n):
		    for j in range(n):
	            matrixA[i][j]=ans[i][j]
	   # print(MatrixA)


 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrixA = []
		matrixB = []
		for _ in range(n):
			matrixA.append(list(map(int,input().split())))
		for _ in range(n):
			matrixB.append(list(map(int,input().split())))
		ob = Solution()
		ob.Mutliply(matrixA, matrixB)
		for i in range(n):
			for j in range(n):
				print(matrixA[i][j], end = " ")
			print()
# } Driver Code Ends
