#Longest Repeating Subsequence
def lcsrepeating(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1] and n!=m:
        t[n][m]=1+lcsrepeating(x,y,n-1,m-1,t)
        return t[n][m]
    else:
        t[n][m]=max(lcsrepeating(x,y,n,m-1,t),lcsrepeating(x,y,n-1,m,t))  
        return t[n][m]
    
x=input()
n=len(x)

t=[[-1 for i in range(n+1)] for j in range(n+1)]
print(lcsrepeating(x,x,n,n,t))