def rotateArr(self,a,D,n):

        if D>n:
          D= D % n
          
        l=a[:D]
        s=a[D:]
       
        ad= s +l
        
        for i in range(0,n):
           a[i]=ad[i]
         