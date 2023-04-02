from collections import deque



class  Node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
    
 
def take_input_level_order( ):
        q=deque()
        print("ENTER the root NODE:")
        rootdata=int(input())
        
        if rootdata==-1:
            return None
        root=Node(rootdata )
        q.append(root ) 
        while q:
            cur_node=q.popleft()
            print("enter the left child of ", cur_node.data)
            left_child=int(input())
            if left_child !=-1:
                left_child=Node(left_child)
                cur_node.left=left_child 
                q.append(left_child)
            print("enter the right child of ", cur_node.data)
            right_child=int(input())
            if right_child !=-1:
                right_child=Node(right_child)
                cur_node.right=right_child 
                q.append(right_child)
        return root     
                
def printinorder1(root)  :
    if root==None:
        return None
    print(root.data)
    printinorder1(root.left)
    printinorder1(root.right)
            
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

root=take_input_level_order()
# printinorder1(root)
printlevelorder(root)