import numpy as np

class Node:
    def __init__(self, state, parent, action, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

class PriorityQueue:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.is_empty():
            raise Exception("Empty Frontier")
        else:
            min_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].path_cost < self.frontier[min_index].path_cost:
                    min_index = i
            node = self.frontier.pop(min_index)
            return node

    def is_empty(self):
        return len(self.frontier) == 0

class EightPuzzleProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = np.array(initial_state).reshape(3, 3)
        self.goal_state = np.array(goal_state).reshape(3, 3)

    def actions(self, state):
        empty_position = np.argwhere(state == 0)[0]
        possible_actions = []

        if empty_position[0] > 0:
            possible_actions.append("Move Up")
        if empty_position[0] < 2:
            possible_actions.append("Move Down")
        if empty_position[1] > 0:
            possible_actions.append("Move Left")
        if empty_position[1] < 2:
            possible_actions.append("Move Right")

        return possible_actions

    def result(self, state, action):
        empty_position = np.argwhere(state == 0)[0]
        new_state = state.copy()

        if action == "Move Up":
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

    def goal_test(self, state):
        return np.array_equal(state, self.goal_state)

    def heuristic(self, state):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_position = np.argwhere(self.goal_state == state[i][j])[0]
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return distance

    def solve(self):
        start = Node(self.initial_state, None, None)
        frontier = PriorityQueue()
        frontier.add(start)

        explored = set()

        while True:
            if frontier.is_empty():
                raise Exception("No solution")
            node = frontier.remove()

            if self.goal_test(node.state):
                actions = []
                while node.parent is not None:
                    actions.append(node.action)
                    node = node.parent
                actions.reverse()
                return actions

            explored.add(tuple(node.state.flatten()))

            for action in self.actions(node.state):
                child_state = self.result(node.state, action)
                child_node = Node(child_state, node, action, node.path_cost + 1 + self.heuristic(child_state))
                if tuple(child_node.state.flatten()) not in explored:
                    frontier.add(child_node)

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
    print("The solution is found using A* algorithm")
    print("Solution:", problem.solve())
