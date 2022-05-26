from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addnode(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsutil(self,v,visited):
        visited.add(v)
        print(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsutil(neighbour,visited)

    def dfs(self,x):
        visited=set()
        self.dfsutil(x,visited)
    
s=Graph()
s.addnode(2,1)
s.addnode(1,4)
s.addnode(2,3)
s.dfs(1)
