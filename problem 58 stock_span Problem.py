
a=[1,3,4,6,8]
def calculateSpan( a ):
        #code here
        s=[]
        ans=[]
        
         
        for i in range(n) :
            while len(s)!=0 and a[s[-1]]<=a[i]:
                s.pop()
            if len(s)==0:
                ans.append(i+1)
            else: 
                top=s[-1]
                ans.append(i-top)
                
            s.append(i)    
            
        return ans
print(calculateSpan( a ))