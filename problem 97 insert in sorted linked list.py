def sortedInsert(self, head,key):
        
        # code here
        # return head of edited linked list
        newnode=Node(key)
        if head is None:
            return newnode
        
        
        else:
            
            
            prev=None
            curr=head
            while curr is not None and curr.data<key:
                prev=curr
                curr=curr.next
            if prev is None:
                newnode.next=curr
                head=newnode
            else:
                prev.next=newnode
                newnode.next=curr
            
            
            
            
        return head