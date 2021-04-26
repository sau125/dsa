def lcsrecursive(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1+lcsrecursive(x,y,n-1,m-1)
    elif x[n-1]!=y[m-1]:
        return max(lcsrecursive(x,y,n,m-1),lcsrecursive(x,y,n-1,m))
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
print(lcsrecursive(x,y,n,m))
print(lcsmemoisation(x,y,n,m,t))

