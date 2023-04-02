
'''A majority element in an array A of size N is an element that appears more than N/2 times in the array.'''
def majorityElement(self, A, N):

       dictionary={}
       for i in range(0,N):
           if A[i] not in dictionary:
               dictionary[A[i]] = 1
           else:
               dictionary[A[i]] += 1
       for value,count in dictionary.items():
           if count > (N/2):
               return value
       return -1  