class Node:
    def __init__(self, data):
        self.visited = False
        self.value = data

    def mark_visited(self):
        self.visited = True

    def is_visited(self):
        return self.visited

num_nodes = int(input("Enter the number of nodes: "))

nodes = []
for x in range(num_nodes):
    nodes.append(Node(x))

graph = {}
for node in nodes:
    neighbors = input(f"Enter neighbors for node {node.value} (comma-separated, or press Enter for no neighbors): ")
    if neighbors:
        neighbor_nodes = [nodes[int(neighbor)] for neighbor in neighbors.split(',')]
        graph[node] = neighbor_nodes
    else:
        graph[node] = []

stack = []

def dfs(stack, graph, start_node: Node, goal_node: Node, path=[]):
    start_node.mark_visited()
    stack.append(start_node)

    while stack:
        current_node = stack.pop()

        if current_node == goal_node:
            path.append(current_node.value)
            return path

        if current_node.value not in path:
            path.append(current_node.value)

        for neighbour_node in graph[current_node]:
            if not neighbour_node.visited:
                neighbour_node.mark_visited()
                stack.append(neighbour_node)
                result = dfs(stack, graph, neighbour_node, goal_node, path)
                if result:
                    return result

start_index = int(input("Enter the starting node index: "))
goal_index = int(input("Enter the goal node index: "))

start_node = nodes[start_index]
goal_node = nodes[goal_index]

path = dfs(stack, graph, start_node, goal_node)

if path:
    print("Path from", start_index, "to", goal_index, ":", path)
else:
    print("No path exists from the source to the goal node.")
