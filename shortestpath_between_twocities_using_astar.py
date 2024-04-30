import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

def euclidean_distance(city1, city2):
    # Since cities are represented as strings, we won't calculate distance
    # Instead, we can just return 0 as a placeholder
    return 0

def get_successors(city, graph):
    return graph.get(city, {}).items()

def a_star(start_city, goal_city, heuristic, successors, graph):
    open_set = []
    closed_set = set()

    start_node = Node(state=start_city, g=0, h=heuristic(start_city, goal_city))
    heapq.heappush(open_set, (start_node.f(), id(start_node), start_node))

    while open_set:
        _, _, current_node = heapq.heappop(open_set)

        if current_node.state == goal_city:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for successor_state, cost in successors(current_node.state, graph):
            if successor_state in closed_set:
                continue

            g = current_node.g + cost
            h = heuristic(successor_state, goal_city)
            successor_node = Node(state=successor_state, parent=current_node, g=g, h=h)

            heapq.heappush(open_set, (successor_node.f(), id(successor_node), successor_node))

    return None  # If no path found

# Example graph representing cities and distances between them
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 8},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 8, 'C': 1}
}

start_city = 'A'
goal_city = 'D'
path = a_star(start_city, goal_city, euclidean_distance, get_successors, graph)
if path:
    print("Shortest path found:", path)
else:
    print("No path found")
