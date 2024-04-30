from collections import defaultdict
from queue import PriorityQueue
class Graph:
    def __init__(self, directed): 
        """Parametrized constructor of class Graph 
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Uniform Cost Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))
g = Graph(False)
g.graph =  defaultdict(list)
g.add_edge('S', 'A', 1)
g.add_edge('S', 'G', 12)
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 1)
g.add_edge('C', 'D', 1)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'G', 2)
g.add_edge('D', 'G', 3)
g.graph
defaultdict(list,
            {'S': [(1, 'A'), (12, 'G')],
             'A': [(1, 'S'), (3, 'B'), (1, 'C')],
             'G': [(12, 'S'), (2, 'C'), (3, 'D')],
             'B': [(3, 'A'), (3, 'D')],
             'C': [(1, 'A'), (1, 'D'), (2, 'G')],
             'D': [(1, 'C'), (3, 'B'), (3, 'G')]})

g.ucs('S', 'G')