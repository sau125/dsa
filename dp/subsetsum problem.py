
def recursive(arr,n,k):
    if n==0:
        return False
    if k==0:
        return True
    if arr[n-1]<=k:
        return recursive(arr,n-1,k-arr[n-1]) or recursive(arr,n-1,k)
    else:
        return recursive(arr,n-1,k)
def subsetmemoize(arr,n,k,t):
    if n==0:
        return 0
    if k==0:
        return 1
    if t[n][k]!=-1:
        return t[n][k]
    if arr[n-1]<=k:
        t[n][k] = (subsetmemoize(arr,n-1,k-arr[n-1],t) or  subsetmemoize(arr,n-1,k,t))
        return t[n][k]
    elif arr[n-1]>k:
        t[n][k] = subsetmemoize(arr,n-1,k,t)
        return t[n][k]
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
t=[[-1 for i in range(k+1)] for j in range(n+1)]
print(recursive(arr,n,k))
print(subsetmemoize(arr,n,k,t))