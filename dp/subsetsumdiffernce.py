
def subsetdiff(arr,n,cal,total):
    if n==0:
        return abs(total-(2*cal))
    if t[n][cal]!=-1:
        return t[n][cal]
    t[n][cal]=min(subsetdiff(arr,n-1,cal+arr[n-1],total),subsetdiff(arr,n-1,cal,total))
    return t[n][cal]
n=int(input())
arr=list(map(int,input().split()))
t=[[-1 for i in range(sum(arr)+1)] for j in range(n+1)]
print(subsetdiff(arr,n,0,sum(arr)))



