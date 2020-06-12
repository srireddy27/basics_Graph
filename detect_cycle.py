from collections import defaultdict 
class Graph: 
   def __init__(self,vertices): 
        self.V= vertices 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def find_parent(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
             return self.find_parent(parent,parent[i]) 
    def union(self,parent,x,y): 
        x_set = self.find_parent(parent, x) 
        y_set = self.find_parent(parent, y) 
        parent[x_set] = y_set 
    def isCyclic(self): 
        parent = [-1]*(self.V) 
        for i in self.graph: 
            for j in self.graph[i]: 
                x = self.find_parent(parent, i)  
                y = self.find_parent(parent, j) 
                if x == y: 
                    return True
                self.union(parent,x,y) 
  
n=int(input("no of vertices"))
g = Graph(n)
for i in range(n):
    u,v=map(int,input().split())
    g.addedge(u,v)
if g.isCyclic(): 
    print "Graph contains cycle"
else : 
    print "Graph does not contain cycle "
