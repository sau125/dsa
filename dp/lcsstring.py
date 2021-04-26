def lcsstringmemoisation(x,y,n,m,t,c):
    if n==0 or m==0:
        return c
    if x[n-1]==y[m-1]:
        t[n][m]=lcsmemoisation(x,y,n-1,m-1,t,c+1)
        return t[n][m]
    elif x[n-1]!=y[m-1]:
        t[n][m]=max(c,max(lcsmemoisation(x,y,n,m-1,t,0),lcsmemoisation(x,y,n-1,m,t,0))) 
        return t[n][m]
    
x=input()
y=input()
n=len(x)
m=len(y)
t=[[-1 for i in range(m+1)] for j in range(n+1)]
c=0
print(lcsmemoisation(x,y,n,m,t,c))
