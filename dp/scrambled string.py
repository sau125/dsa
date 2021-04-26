def scrambled(a,b):
    if len(a)!=len(b):
        return False
    if a==b:
        return True
    elif len(a)<=1:
        return False
    n=len(a)
    ans=False
    for i in range(1,n):
        if (scrambled(a[:i],b[-i:]) and scrambled(a[i:],b[:-i])) or (scrambled(a[:i],b[:i]) and scrambled(a[i:],b[i:])):
            ans=True
            break
    return ans

    
a=input()
b=input()
print(scrambled(a,b))