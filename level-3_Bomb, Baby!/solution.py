# py 2.7
def solution(sx,sy):
    X,Y=int(sx),int(sy)
    x=max(X,Y)
    y=min(X,Y)
    c=0
    while y!=1:
        
        if y==0:
            return "impossible"
        c+=int(x/y)
        x,y=y, x%y
    
    # greater than 1, beshi value reduce korbe
    c+=(x-1)
    # print(c)
    return str(c)
        
# solution('2', '1')