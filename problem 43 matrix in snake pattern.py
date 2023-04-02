def snakePattern(self, matrix): 

        ans=[]
        for i in range(n):
           l=[]
           for j in range(n):
                l.append(matrix[i][j])
            
           if i%2==0 or i==0:  
               ans.append(l)
           else:
                
               ans.append(l[::-1])
        
        # ans.append(l)  
        s=[]
        for i in range(n):
            for j in range(n):
                s.append(ans[i][j])
        
        return s