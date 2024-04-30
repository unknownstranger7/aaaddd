from collections import deque

def waterjug_bfs(m, n, d):
    # Set up initial state
    initial_state = (0, 0)
    visited = set()
    queue = deque([(initial_state, [])])  # Queue of tuples: (state, path)

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        # Check if goal state is reached
        if d in current_state:
            if current_state[0] == d:
                print("Fill jug 1")
            elif current_state[1] == d:
                print("Fill jug 2")
            print("Steps:", path)
            return

        # Generate successor states
        a, b = current_state
        successors = [
            (m, b),  # Fill jug 1
            (a, n),  # Fill jug 2
            (0, b),  # Empty jug 1
            (a, 0),  # Empty jug 2
            (min(a + b, m), max(0, a + b - m)),  # Pour from jug 2 to jug 1
            (max(0, a + b - n), min(a + b, n)),  # Pour from jug 1 to jug 2
        ]
        
        # Add valid successors to the queue
        for successor_state in successors:
            if successor_state not in visited:
                queue.append((successor_state, path + [successor_state]))

    print("No solution found.")

# Given scenario
m = 5  # Capacity of jug 1
n = 3  # Capacity of jug 2
d = 4  # Desired amount of water
waterjug_bfs(m, n, d)
