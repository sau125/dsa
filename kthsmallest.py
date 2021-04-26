import heapq 
def kthsmallest(n,arr,k):
    heapq.heapify(arr)
    for i in range(k):
        temp=heapq.heappop(arr)
    return temp
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
print(kthsmallest(n,arr,k))
