def addNode(head, p, data):
    newnode=Node(data)
    
    if head is None :
        head=newnode
         
        return head
    
    curr=head
    prev=None
    count=0
    while count<=p and curr:
        prev=curr
        curr=curr.next
        count=count+1
    if  prev is None:
         newnode.next=curr
         newnode.prev=prev
         head.prev=newnode
         head=newnode
          
         
         return head
         
    
    newnode.next=curr
    prev.next=newnode
    newnode.prev=prev
     
    
    return head
        