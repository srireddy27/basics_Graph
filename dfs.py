from collections import defaultdict
class Graph:
    dict1=defaultdict(list)
    def addedge(self,u,v):
        Graph.dict1[u].append(v)
    def print(self):
        return "Adjacency List for given is {}".format(list(Graph.dict1.items()))
    def dfs(self,s):
        visited=[0]*(len(Graph.dict1))
        self.dfsprint(visited,s)
    def dfsprint(self,visited,v):
        visited[v]=1
        print(v,end=" ")
        for i in Graph.dict1[v]:
            if(visited[i]==0):
                self.dfsprint(visited,i)


obj=Graph()
n=int(input("Enter the no of Edges: "))
for i in range(n):
    u,v=map(int,input().split())
    obj.addedge(u,v)
print(obj.print())
obj.dfs(int(input("Enter the starting source")))
