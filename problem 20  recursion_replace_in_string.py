s="uiabcada"

def ris(s,a,b):
     
    if len(s)==0:
        return s
    smallouput=ris(s[1:],a,b)
    if s[0]==a:
       return  b + smallouput
    else:
        return s[0] + smallouput 
print(ris(s,"a","b"))

s="piaeiuroauopirppirpirpipppoi"
def rispi(s):
    if len(s)==0 or len(s)==1:
        return s 
    if s[0]=="p" and s[1]=="i":
        smalloutput=rispi(s[2:])
        return "3.14" + smalloutput
    else:
        smalloutput=rispi(s[1:])
        
        
        return s[0] + smalloutput
print(rispi(s))    