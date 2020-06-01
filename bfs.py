from collections import defaultdict
class Graph:
    dict1=defaultdict(list)
    def addedge(self,u,v):
        Graph.dict1[u].append(v)
    def print(self):
        return "Adjacency List for given is {}".format(list(Graph.dict1.items()))
    def bfs(self,s):
        visited=[0]*(len(Graph.dict1))
        queue=[]
        queue.append(s)
        visited[s]=1
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in Graph.dict1[s]:
                if(visited[i]==0):
                    queue.append(i)
                    visited[i]=1
    
obj=Graph()
n=int(input("Enter the no of Edges: "))
for i in range(n):
    u,v=map(int,input().split())
    obj.addedge(u,v)
print(obj.print())
obj.bfs(int(input("Enter the starting source")))

        
