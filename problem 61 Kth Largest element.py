arr = [1, 2, 12, 9, 30, 2, 50]
def kLargest(self,arr, n, k):
        arr.sort(reverse=True)
        x=[]
        for i in range(0,k):
            x.append(arr[i])
        return x   
print(kLargest(arr))