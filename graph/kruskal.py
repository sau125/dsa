# krushkal algorthm
def find(parent,u):
    if parent[u]==-1:
        return u
    return find(parent,parent[u])
def union(parent,rank,x,y):
    xroot=find(parent,x)
    yroot=find(parent,y)
    if rank[xroot]>rank[yroot]:
        parent[yroot]=xroot
    elif rank[xroot]<rank[yroot]:
        parent[xroot]=yroot
    elif rank[xroot]==rank[yroot]:
        parent[xroot]=yroot
        rank[yroot]+=1
def kruskal(v,graph):
    result=[]
    parent=[-1]*v
    rank=[0]*v
    sorted(graph,key=lambda item:item[2])
    res=0
    i=0
    while res<v-1:
        u,v,w=graph[i]
        i+=1
        x=find(parent,u)
        y=find(parent,v)
        if x!=y:
            result.append([u,v,w])
            e+=1
            union(parent,rank,x,y)