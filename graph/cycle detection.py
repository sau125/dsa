
# detect cycle
def union(parent,x,y):
    parent[x]=y
def find_parent(parent,p):
    if parent[p]==-1:
        return p
    return find_parent(parent,parent[i])
def cycle(v,graph):
    parent=[-1]*v:
        for i in range(v):
            for j in range(v):
                x=find_parent(parent,i)
                y=find_patern(patern,j)
                if x==y:
                    return True
                union(parent,x,y)
                