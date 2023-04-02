def sumTriangles(self,matrix, n):
        # code here 
        ans=[]
        su=0
        sl=0
        for i in range(n):
            for j in range(n):
                if i<=j:
                    su+=matrix[i][j]
                    # print(su,i,j)
                if i>=j:
                    sl+=matrix[i][j]
                    
                    # print(sl,i,j)
        ans.append(su)
        ans.append(sl)
        return ans