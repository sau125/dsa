def diametr(node,res):
    if root is None:
        return 0
    l=diameter(node.left,res)
    r=diameter(node.right,res)
    temp=1+max(l,r)
    ans=max(temp,1+l+r)
    res=max(ans,res)
n=int(input())
for i in range(n):
    