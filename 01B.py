class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def addEdge(self, u, v):
        if u not in self.graph_dict:
            self.graph_dict[u] = [v]
        else:
            self.graph_dict[u].append(v)

    def bfs(self, s):
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        q = queue()
        q.enqueue(s)
        visited[s] = True
        while not q.isEmpty():
            s = q.dequeue()
            print(s, end=" ")
            for i in self.graph_dict[s]:
                if visited[i] == False:
                    q.enqueue(i)
                    visited[i] = True
        print()

    def printGraph(self):
        print(self.graph_dict)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()
g.bfs(2)