def detectLoop(self, head):
        mp=set()
        cur=head
        
        while cur:
            # print(mp)
            if cur  in mp:
                return True
            mp.add(cur)
            cur=cur.next
        
        return False 
    
    