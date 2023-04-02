s="ajdljbbcgccjaa"
def rcds(s):
    if len(s)==1 or len(s)==0:
        return s 
    if s[0]== s[1]:
        smalloutput=rcds(s[2:])
        return s[0] + smalloutput
    else:
        smalloutput=rcds(s[1:])
        return  s[0] +smalloutput
    
print(rcds(s))