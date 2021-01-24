# Python Program to detect cycle in an undirected graph
from collections import defaultdict

# This class represents a undirected
# graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):
        #we have now visited this node
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                #keep going
                if self.isCyclicUtil(i, visited, v):
                    return True
            elif parent is not i:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.V
        parent = None
        for i in range(self.V):
            if visited[i] is False:
                if self.isCyclicUtil(i, visited, parent) is True:
                    return True
        return False


g = Graph(6)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

'''    
g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)

if g1.isCyclic():
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")
'''
#This code is contributed by Neelam Yadav
