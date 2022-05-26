from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph=defaultdict(list)
        
    def addnode(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print(self.graph)

    def dfutil(self,visited,v):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfutil(visited,i)


    def dfs(self,x):
        visited=set()
        self.dfutil(visited,x)

s1=Graph()
s1.addnode(2,1)
s1.addnode(2,3)
s1.dfs(2)
s1.display()