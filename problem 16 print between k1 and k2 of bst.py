

def printNearNodes(self, root, low, high):
        arr=[]
        def printNearNode( root,low,high):
            if root==None:
                return 
            elif root.data<low :
                printNearNode(root.right,low,high)
            
            elif root.data> high:
                printNearNode(root.left,low,high) 
             
            
            else:
                 
                arr.append(root.data)
                
                printNearNode(root.left,low,high)
                printNearNode(root.right,low,high)
        printNearNode(root,low,high)
    
         
        return arr 