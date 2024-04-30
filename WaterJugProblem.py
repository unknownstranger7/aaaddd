from collections import deque

def WaterJugProblem(m, n, d):
    visited_states = set()
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        if current_state[0] == d or current_state[1] == d:
            print("Solution Found!")
            path_printing(initial_state, current_state, path)
            return

        # Fill jug 1
        Jug1_filling = (m, current_state[1])
        if Jug1_filling not in visited_states:
            queue.append((Jug1_filling, path + [(current_state, Jug1_filling)]))

        # Fill jug 2
        Jug2_filling = (current_state[0], n)
        if Jug2_filling not in visited_states:
            queue.append((Jug2_filling, path + [(current_state, Jug2_filling)]))

        # Empty jug 1
        empty_jug1 = (0, current_state[1])
        if empty_jug1 not in visited_states:
            queue.append((empty_jug1, path + [(current_state, empty_jug1)]))

        # Empty jug 2
        empty_jug2 = (current_state[0], 0)
        if empty_jug2 not in visited_states:
            queue.append((empty_jug2, path + [(current_state, empty_jug2)]))

        # Pour water from jug 1 to jug 2
        pour_jug1_to_jug2 = (max(0, current_state[0] - (n - current_state[1])), min(n, current_state[1] + current_state[0]))
        if pour_jug1_to_jug2 not in visited_states:
            queue.append((pour_jug1_to_jug2, path + [(current_state, pour_jug1_to_jug2)]))

        # Pour water from jug 2 to jug 1
        pour_jug2_to_jug1 = (min(m, current_state[0] + current_state[1]), max(0, current_state[1] - (m - current_state[0])))
        if pour_jug2_to_jug1 not in visited_states:
            queue.append((pour_jug2_to_jug1, path + [(current_state, pour_jug2_to_jug1)]))

    print("No solution found.")

def path_printing(initial_state, final_state, path):
    for transition in path:
        from_state, to_state = transition
        print(f"{from_state} -> {to_state}")
    print(final_state)

# def get_previous_state(current_state):
#     return (current_state[0] + current_state[1], current_state[1]) if current_state[0] > 0 else (0, current_state[0] + current_state[1])

# Get user inputs
m = int(input("m: "))
n = int(input("n:"))
d = int(input("d:"))

# Solve the Water Jug Problem
WaterJugProblem(m, n, d)