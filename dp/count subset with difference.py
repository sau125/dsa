#count subset with difference
def subset(arr,n,k,t):
    if n==0:
        return 0
    if k==0:
        return 1
    if t[n][k]!=-1:
        return t[n][k]
    if arr[n-1]<=k:
        t[n][k]=max((1+subset(arr,n-1,k-arr[n-1],t)),subset(arr,n-1,k,t))
        return t[n][k]
    elif arr[n-1]>k:
        t[n][k]=subset(arr,n-1,k,t)
        return t[n][k]
n=int(input())
d=int(input())

arr=list(map(int,input().split()))
x=sum(arr)
if (x+d)%2!=0:
    print("Not possible")
else:
    k=int((x+d)/2)    
    t=[[-1 for i in range(k+1)] for j in range(n+1)]
    print(subset(arr,n,k,t))