import numpy as np

# Define the initial and goal states
start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# Initialize the lists to keep track of visited, open, and closed states
visited = []
open_list = []
closed = []
closed.append(start_state)

def heuristic(state, goal_state):
    """
    Calculate the heuristic value for a given state.
    The heuristic is the number of tiles that are not in their correct position.
    """
    res = state == goal_state
    return 9 - np.count_nonzero(res)

def possible_children(state, goal_state):
    """
    Generate the possible next states (children) from the current state.
    This is done by moving the empty tile (0) in different directions.
    """
    visited.append(state)  # Add the current state to the visited list

    # Find the position of the empty tile (0)
    [i], [j] = np.where(state == 0)

    # Define the possible directions to move the empty tile
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    children = []
    for direction in directions:
        ni = i + direction[0]
        nj = j + direction[1]
        new_state = state.copy()  # Create a copy of the current state

        # Check if the new position is within the 3x3 grid
        if 0 <= ni <= 2 and 0 <= nj <= 2:
            # Swap the empty tile with the tile in the new position
            new_state[i, j], new_state[ni, nj] = new_state[ni, nj], new_state[i, j]

            # Check if the new state has not been visited before
            if not any(np.array_equal(new_state, visited_state) for visited_state in visited):
                visited.append(new_state)  # Add the new state to the visited list
                new_heuristic = heuristic(new_state, goal_state)  # Calculate the heuristic value
                children.append([new_heuristic, new_state])  # Add the new state to the children list

    # Sort the children list by the heuristic value
    children = sorted(children, key=lambda x: x[0])

    # Extract the new states from the sorted children list
    for i in range(len(children)):
        children[i] = children[i][1]

    return children

def main(start_state, goal_state):
    """
    The main function that implements the A* search algorithm.
    """
    start_heuristic = heuristic(start_state, goal_state)

    # Check if the start state is the goal state
    if start_heuristic == 0:
        for node in closed:
            print(node)
        return True
    else:
        # Generate the possible children states
        children = possible_children(start_state, goal_state)

        # If there are children states
        if len(children) > 0:
            for i in range(len(children)):
                open_list.insert(i, children[i])  # Add the children to the open list

            # If the open list is not empty
            if len(open_list) > 0:
                new_heuristic = heuristic(open_list[0], goal_state)
                new_state = open_list[0]
                closed.append(open_list[0])  # Add the new state to the closed list
                open_list.pop(0)  # Remove the new state from the open list

                # Check if the new state is the goal state
                if new_heuristic == 0:
                    for node in closed:
                        print(node)
                    return True
                else:
                    # Recursively call the main function with the new state
                    main(new_state, goal_state)
        else:
            return False

# Run the main function with the start and goal states
if __name__ == "__main__":
    main(start_state, goal_state)