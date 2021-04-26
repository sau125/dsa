#bfs of graph
def bfs(s,graph):
    visited=[False]*len(graph)
    q=[]
    q.append(s)
    visited[s]=True
    while q:
        r=q.pop(0)
        print(r)
        for i in graph[r]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
def dfsutil(s,graph,visited):
    visited[s]=True
    print(s)
    for i in graph[s]:
        if visited[i]==False:
            dfsutil(i,graph,visited)
def dfs(s,graph):
    visited=[False]*len(graph)
    dfsutil(s,graph,visited)