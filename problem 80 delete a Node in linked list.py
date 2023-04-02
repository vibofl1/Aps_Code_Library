def delNode(head, k):
    
    prev=None
    curr=head
    count=0
   
    while count<k-1:
        prev=curr
        curr=curr.next
        count=count+1
    if prev is None:
        return head.next

    prev.next=curr.next
    return head