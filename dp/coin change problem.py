def changecoin(coin,n,s,t):
    if n==0:
        return 0
    if s==0:
        return 1
    if t[n][s]!=-1:
        return t[n][s]
    if coin[n-1]<=s:
        t[n][s]=changecoin(coin,n,s-coin[n-1],t)+changecoin(coin,n-1,s,t)
        return t[n][s]
    elif coin[n-1]>s:
        t[n][s]=changecoin(coin,n-1,s,t)
        return t[n][s]
n=int(input())
s=int(input())
arr=list(map(int,input().split()))
t=[[-1 for i in range(s+1)] for j in range(n+1)]
print(changecoin(arr,n,s,t))