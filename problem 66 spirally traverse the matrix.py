 

class Solution:
    

    def spirallyTraverse(self,arr, r, c): 
         
        ans=[]
        top,left,right,bottom=0,0,c-1,r-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                ans.append(arr[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(arr[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(arr[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(arr[i][left])
                left+=1
        return ans


 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()
 