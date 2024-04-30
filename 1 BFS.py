class Node:
    def __init__(self, data):
        self.visited = False
        self.value = data
        self.parent = None  # Parent node attribute added

    def now_visited(self):
        # Method to mark the node as visited
        self.visited = True

    def is_visited(self):
        # Method to check if the node is visited
        return self.visited

num_nodes = int(input("Enter the number of nodes: "))

nodes = []
for x in range(num_nodes):
    nodes.append(Node(x))

graph = {}
# Create the graph
for node in nodes:
    neighbors = input(f"Enter neighbors for node {node.value} (comma-separated, or press Enter for no neighbors): ")
    if neighbors:
        neighbor_nodes = [nodes[int(neighbor)] for neighbor in neighbors.split(',')]
        graph[node] = neighbor_nodes
    else:
        graph[node] = []

queue = []

def bfs(queue, graph, start_node: Node, goal_node: Node):
    # Method to perform Breadth First Search
    start_node.now_visited()
    # Mark the start node as visited and add it to the queue
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)

        if current_node == goal_node:
            path = []  # List to store the shortest path
            while current_node is not None:
                path.insert(0, current_node.value)
                current_node = current_node.parent
            return path

        for neighbour_node in graph[current_node]:
            if not neighbour_node.visited:
                neighbour_node.now_visited()
                neighbour_node.parent = current_node  # Set parent node
                queue.append(neighbour_node)

start_index = int(input("Enter the starting node index: "))
goal_index = int(input("Enter the goal node index: "))

shortest_path = bfs(queue, graph, nodes[start_index], nodes[goal_index])
if shortest_path:
    print("Shortest path:", shortest_path)
else:
    print("No path exists from the source to the goal node.")
