def minkey(key,msset,v):
    mins=2**31-1
    for i in range(v):
        if key[i]<mins and msset==False:
            mins=key[i]
            min_index=i
    return min_index
def prim(v,graph):
    max_int=2**31-1
    key=[max_int]*v
    key[0]=0
    parent=[None]*v
    msset=[False]*v
    for i in range(v):
        m=minkey(key,msset,v)
        msset[m]=True
        for j in range(v):
            if msset[j]==False and key[j]>graph[m][j] and graph[m][j]>0:
                key[j]=graph[m][i]
                parent[j]=m