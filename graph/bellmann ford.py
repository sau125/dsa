def bellmannford(graph,v,s):
    dis=[float"Inf"]*v
    dis[0]=0
    for i in range(v-1):
        for u,v,w in graph:
            if dis[u]!=float"Inf" and dis[v]>dis[u]+w:
                dis[v]=dis[u]+w
    for u,v,w in graph:
        if dis[u]!=float"Inf" and dis[v]>dis[u]+w:
            return "There exist a cycle"
            break