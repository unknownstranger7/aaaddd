import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_node, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put(next_node, priority)
                came_from[next_node] = current

    return came_from, cost_so_far

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 3},
    'D': {}
}

start_node = 'A'
goal_node = 'D'
came_from, cost_so_far = uniform_cost_search(graph, start_node, goal_node)


path = []
current = goal_node
while current != start_node:
    path.append(current)
    current = came_from[current]
path.append(start_node)
path.reverse()

print("Path:", path)
print("Cost:", cost_so_far[goal_node])
