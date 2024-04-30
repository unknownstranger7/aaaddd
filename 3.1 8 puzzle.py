import numpy as np

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.frontier)
    
    def isEmpty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.isEmpty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.isEmpty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        

# The unhashable type: 'numpy.ndarray' error is fixed by converting the state to a tuple in the line 54 and 58

class EightPuzzleProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = np.array(initial_state).reshape(3, 3)
        self.goal_state = np.array(goal_state).reshape(3, 3)


	# This method returns a list of possible actions on a given state
    def actions(self, state):

        # empty_position stores the position of the empty tile
        empty_position = np.argwhere(state == 0)[0]

        possible_actions = []

        # If the emtpy tile is not in the first row then we can move it up
        if empty_position[0] > 0:
            possible_actions.append("Move Up")

        # If the emtpy tile is not in the last row then we can move it down
        if empty_position[0] < 2:
            possible_actions.append("Move Down")

        # If the emtpy tile is not in the first column then we can move it left
        if empty_position[1] > 0:
            possible_actions.append("Move Left")

        # If the emtpy tile is not in the last column then we can move it right
        if empty_position[1] < 2:
            possible_actions.append("Move Right")

        return possible_actions

	# This method returns the new state after applying the given action on the given state
    def result(self, state, action):

        # empty_position stores the position of the empty tile in the form of a list 
        empty_position = np.argwhere(state == 0)[0]
        new_state = state.copy()

        if action == "Move Up":

            # The empty tile is swapped with the tile above it and the new state is returned
            new_state[empty_position[0]][empty_position[1]] = state[empty_position[0] - 1][empty_position[1]]
            new_state[empty_position[0] - 1][empty_position[1]] = 0

        elif action == "Move Down":
            new_state[empty_position[0]][empty_position[1]] = state[empty_position[0] + 1][empty_position[1]]
            new_state[empty_position[0] + 1][empty_position[1]] = 0

        elif action == "Move Left":
            new_state[empty_position[0]][empty_position[1]] = state[empty_position[0]][empty_position[1] - 1]
            new_state[empty_position[0]][empty_position[1] - 1] = 0

        elif action == "Move Right":
            new_state[empty_position[0]][empty_position[1]] = state[empty_position[0]][empty_position[1] + 1]
            new_state[empty_position[0]][empty_position[1] + 1] = 0

        return new_state
    
	
	# This method checks if the given state is the goal state
    def goal_test(self, state):
        return np.array_equal(state, self.goal_state)


	# This method solves the problem using the given strategy
    # This method solves the problem using the given strategy
    def solve(self, strategy):
        start = Node(self.initial_state, None, None)
        frontier = strategy()
        frontier.add(start)

        explored = set()

        while True:
            if frontier.isEmpty():
                raise Exception("No solution")
            node = frontier.remove()

            if self.goal_test(node.state):
                if strategy == StackFrontier:
                    print("The solution is found using DFS")
                elif strategy == QueueFrontier:
                    print("The solution is found using BFS")

                actions = []

                while node.parent is not None:
                    actions.append(node.action)
                    node = node.parent

                actions.reverse()
                return actions

            # Add the state to the explored set if it is not already in it and flatten the state to convert it to a tuple
            explored.add(tuple(node.state.flatten()))  # Convert to tuple

            if strategy == StackFrontier:
                for action in reversed(self.actions(node.state)):
                    child = Node(self.result(node.state, action), node, action)
                    if not frontier.contains_state(child.state) and tuple(child.state.flatten()) not in explored:
                        frontier.add(child)

            elif strategy == QueueFrontier:
                for action in self.actions(node.state):
                    child = Node(self.result(node.state, action), node, action)
                    if not frontier.contains_state(child.state) and tuple(child.state.flatten()) not in explored:
                        frontier.add(child)

            else:
                raise Exception("Invalid Strategy")


def create_puzzle():
    print("Enter the initial state of the puzzle (use numbers 0-8 to represent the tiles, 0 for the blank tile):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    print("Enter the goal state of the puzzle (use numbers 0-8 to represent the tiles, 0 for the blank tile):")
    goal_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)

    return initial_state, goal_state

if __name__ == "__main__":
    initial_state, goal_state = create_puzzle()
    problem = EightPuzzleProblem(initial_state, goal_state)

    print("Solution:", problem.solve(StackFrontier))


    print("Solution:", problem.solve(QueueFrontier))



