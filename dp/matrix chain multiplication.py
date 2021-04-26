# matrix chain multiplication
def matmax(arr,i,j):
    if i>=j:
        return 0
    ans=2**31-1
    for k in range(i,j):
        temp=matmax(arr,i,k)+matmax(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp<ans:
            ans=temp
    return ans   
def matmaxmemoize(arr,i,j,t):
    if i>=j:
        return 0
    ans=2**31-1
    if t[i][j]!=-1:
        return t[i][j]
    for k in range(i,j):
        temp=matmaxmemoize(arr,i,k,t)+matmaxmemoize(arr,k+1,j,t)+(arr[i-1]*arr[k]*arr[j])
        if temp<ans:
            ans=temp
    t[i][j]=ans
    return t[i][j]
arr=list(map(int,input().split()))
n=len(arr)
ans=2**31-1
print(matmax(arr,1,n-1))
t=[[-1 for i in range(n+1)] for j in range(n+1)]
print(matmaxmemoize(arr,1,n-1,t))