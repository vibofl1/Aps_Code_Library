from collections import deque

class Node:
    def __init__(self,key)  :
        self.key=key
        self.left=None
        self.right=None
    
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(38)
root.right.right(50)
def printlevelorder(root)      :
     q=deque()
     q.append(root )

     while q :
        print (q)
         
        cur_node=q.popleft()
         
        if cur_node.left :
            q.append(cur_node.left)
            print(cur_node.data,"left is" , cur_node.left.data)
        if cur_node.right:
            q.append(cur_node.right)
            print(cur_node.data,"right is ", cur_node.right.data )
            
printlevelorder(root)   

         