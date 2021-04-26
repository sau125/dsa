def subset(arr,n,s,t):
    if n==0:
        return 0
    if s==0:
        return 1
    if t[n][s]!=-1:
        return t[n][s]
    if arr[n-1]<=s:
        t[n][s]=(subset(arr,n-1,s-arr[n-1],t) )or subset(arr,n-1,s,t)
        return t[n][s]
    elif arr[n-1]>s:
        t[n][s]=subset(arr,n-1,s,t)
        return t[n][s]
def equalsum(arr,n):
    S=sum(arr)
    if S%2!=0:
        return 0
    else:
        s1=S//2
        t=[[-1 for i in range(s1+1)] for j in range(n+1)]
        r=subset(arr,n,s1,t)
        return r
n=int(input())
arr=list(map(int,input().split()))
print(equalsum(arr,n))