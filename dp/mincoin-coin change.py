def mincoin(arr,s,n,t):
    if s==0:
        return 0
    if n==0:
        return 2**31-2
    if t[n][s]!=-1:
        return t[n][s]
    if arr[n-1]<=s:
        t[n][s]=min((1+mincoin(arr,s-arr[n-1],n,t)),mincoin(arr,s,n-1,t))
        return t[n][s]
    elif arr[n-1]>s:
        t[n][s]=mincoin(arr,s,n-1,t)
        return t[n][s]
n=int(input())
s=int(input())
arr=list(map(int,input().split()))
t=[[-1 for i in range(s+1)] for j in range(n+1)]
print(mincoin(arr,s,n,t))    