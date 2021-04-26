#adjacency list of graph
class adjnode:
    def __init__(self,data):
        self.vertex=data
        self.next=None
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V
    def addedge(self,src,desc):
        node=adjnode(desc)
        node.next=self.graph[src]
        self.graph[src]=node
        #add src node to destination node
        node=adjnode(src)
        node.next=self.graph[desc]
        self.graph[desc]=node
   def print_graph(self):
       
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

# stl representation of graph
def addedge(ajdlist,u,v):
    adjlist[u].append(v)
    adjlist[v].append(u)
    
adj=[[] for i in range(v)]
          
        