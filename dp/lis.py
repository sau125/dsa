def lis(arr,i,n,prev):
    if i==n:
        return 0
    if arr[i]>prev:
        return 1+lis(arr,i+1,n,arr[i])
    else:
        return lis(arr,i+1,n,prev)
arr=list(map(int,input().split()))
n=int(input())
print(lis(arr,0,n,-2**32))