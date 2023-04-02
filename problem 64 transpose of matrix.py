def transpose(self,arr, n):
        j=0
        for i in range(n):
            for j in range(0,  j<=i):
                if j<i:
                    arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
                    # print (arr[i][j],arr[j][i])
                
        return arr