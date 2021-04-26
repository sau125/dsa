def partition(arr,start,end):
    pindex=start
    pivot=arr[end]
    for i in range(start,end):
        if arr[i]<=pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex
def quick(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quick(arr,start,pi-1)
        quick(arr,pi+1,end)
arr=list(map(int,input().split()))
quick(arr,0,len(arr)-1)
for i in arr:
    print(i,end=" ")
    