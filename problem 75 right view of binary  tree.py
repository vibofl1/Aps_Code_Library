def ll(self,root,level):
            if root ==None:
                return None
            
            if level==len(self.res):
                self.res.append(root.data)
             
            self.ll(root.right,level+1)
            self.ll(root.left,level+1)
    def rightView(self,root):
        self.res=[]
         
        
            
        self.ll(root,0)
        # print(res,res1)
        return self.res
