def search(self,matrix, n, m, x): 
    	# code here 
    	i=0
    	j=m-1
    	
    	while (i<n and j>=0):
    	     if matrix[i][j]==x:
    	         return 1
    	     elif matrix[i][j]< x:
    	          i+=1
    	     elif matrix[i][j]>x:
    	         j-=1
        
    	return 0   