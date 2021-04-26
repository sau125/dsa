def eggdroping(e,f):
    if e==1:
        return f
    if f==0 or f==1:
        return f
    x=2**31-1
    for k in range(1,f+1):
        temp=1+max(eggdroping(e-1,k-1),eggdroping(e,f-k))
        x=min(x,temp)
    return x
def eggmemoise(e,f,t):
    if e==1:
        return f
    if f==0 or f==1:
        return f
    if t[e][f]!=-1:
        return t[e][f]
    x=2**31-1
    for k in range(1,f+1):
        temp=1+max(eggmemoise(e-1,k-1,t),eggmemoise(e,f-k,t))
        x=min(x,temp)
    t[e][f]=x 
    return t[e][f]
    
e=int(input())
f=int(input())
print(eggdroping(e,f))
t=[[-1 for i in range(f+1)] for j in range(e+1)]
print(eggmemoise(e,f,t))