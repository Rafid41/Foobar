# py 2.7
def solution(l):
    ops=[]
    for s in l:

        s=s.split('.')
        lst=[]

        if(len(s)>=1):
            lst.append(int(s[0]))
        
        if(len(s)>=2):
            lst.append(int(s[1]))
            
        if(len(s)>=3):
            lst.append(int(s[2]))

        ops.append(lst)
        
        
        
    ops.sort()
   
    for i in range(len(ops)):
        
        if(len(ops[i])==1):
            ops[i]=str(ops[i][0])
        
        elif(len(ops[i])==2):
            ops[i]=str(ops[i][0])+'.'+str(ops[i][1])
        
        elif(len(ops[i])==3):
            ops[i]=str(ops[i][0])+'.'+str(ops[i][1])+'.'+str(ops[i][2])
    
    print(ops)
    return ops
        
    
    
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])


