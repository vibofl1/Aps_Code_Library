#creation of Linked list and basic  Crud operations using recursion and without recursion   

arr=[1,2,3,4,5,-1] 


class Node:
    def __init__( self,data)  :
        self.data=data 
        self.next=None 
        
    
    def create(arr):
        head=None
          
        curr=Node(arr[0])
        for x in arr:
            if x== -1 :
                break 
            
            newnode =Node(x)
            if head is None:
                head=newnode
            else:
                curr=head 
            while curr.next is not None:
                curr=curr.next
            curr.next=newnode
        return head 
    def create2 (arr):
        head=None
        for x in  arr:
            if x==-1: break 
            newnode=Node(x)
             
            if head is None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
        return head 
         
    def printll(head):
        while head is not None:
            print(str(head.data )+  " -> ",end=" ")
            head=head.next 
        print("None")
        return 
    
    def delete(head,i) :
        prev=None
        curr=head
        while i>1 and curr is not None:
            prev=curr
            curr=curr.next
            i-=1
        prev.next=curr.next 
        return head
    
    def insertr( head,i,data):
        if i==0:
            newnode=Node(data)
            newnode.next=head 
            return newnode
        if head is None:
            return None
        small=Node.insertr(head.next,i-1,data)
        head.next=small
        
        return head  
    
    
    def deleter (head,i):
        if i==0:
            head=head.next 
        small = Node.deleter(head.next,i-1)
        head.next=small 
        return 
    def 
            
            
                       
head=Node.create2(arr)
Node.printll(head) 
Node.insertr( head,1,90)
Node.printll(head)
Node.delete(head,2)  
# Node.insert(head,2,2)
Node.insertr( head,1,20)
Node.printll(head)
Node.delete(head,2)
Node.printll(head)


         
    
    
     
                
                
            
            
            
            
         

         
            
        
    
        
    
    
        