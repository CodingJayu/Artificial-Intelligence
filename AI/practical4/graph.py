from collections import defaultdict

from matplotlib.style import available

class graph():
    
    def __init__(self):
        self.graph=defaultdict(list)
        

    def addnode(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def color(self):
        print(self.graph)
        size=4
        result=[-1] * size

        result[0]=0

        for i in range(1,size):
            temp=[]
            for el in self.graph[i]:
                temp.append(result[el])
            temp.sort()
            z=0
            while(True):
                if(z not in temp):
                    result[i]=z
                    break
                z=z+1


        for u in range(size):
            print(u,"----> Colour",result[u])

s1=graph()
s1.addnode(0,1)
s1.addnode(0,2)
s1.addnode(2,3)
s1.addnode(2,1)
s1.addnode(1,3)
s1.color()

    