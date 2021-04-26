def countsubset(arr,k,n,t):
    if n==0:
        return 0
    if k==0:
        return 1
    if arr[n-1]<=k:
        t[n][k]=max(1+countsubset(arr,k-arr[n-1],n-1,t),countsubset(arr,k,n-1,t))
        return t[n][k]
    elif arr[n-1]>k:
        t[n][k]=countsubset(arr,k,n-1,t)
        return t[n][k]
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
t=[[-1 for i in range(k+1)] for j in range(n+1)]
print(countsubset(arr,k,n,t))