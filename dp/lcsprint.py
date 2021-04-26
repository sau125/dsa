#lcs print memoize
def lcsmemoisation(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        t[n][m]=1+lcsmemoisation(x,y,n-1,m-1,t)
        return t[n][m]
    elif x[n-1]!=y[m-1]:
        t[n][m]=max(lcsmemoisation(x,y,n,m-1,t),lcsmemoisation(x,y,n-1,m,t))  
        return t[n][m]
    
x=input()
y=input()
n=len(x)
m=len(y)
t=[[-1 for i in range(m+1)] for j in range(n+1)]
lcsmemoisation(x,y,n,m,t)
a=n
b=m
r=""
while a>0 and b>0:
    if t[a][b]==t[a][b-1]:
        b-=1
    if t[a][b]==t[a-1][b]:
        a-=1
    else:
        r=r+x[a-1]
        a-=1
        b-=1
print(r[::-1]) 
    
