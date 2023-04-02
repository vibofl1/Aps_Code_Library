def LeftView( root):
        res=[]
        def ll(root,level):
            if root ==None:
                return None
            
            if level==len(res):
                res.append(root.data)
             
            ll(root.left,level+1)
            ll(root.right,level+1)
        
            
        ll(root,0)
        # print(res,res1)
        return res
