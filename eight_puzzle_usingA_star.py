import heapq
import itertools

# Define the goal state for the 8-puzzle
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty tile

# Define the movements of the empty tile
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down

# Function to find the coordinates of a value in the puzzle
def find_coord(puzzle, value):
    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == value:
                return i, j
    return None, None

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                target_i, target_j = divmod(puzzle[i][j] - 1, 3)
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

# Function to generate possible moves
def generate_moves(puzzle):
    empty_i, empty_j = find_coord(puzzle, 0)
    for di, dj in MOVES:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[empty_i][empty_j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[empty_i][empty_j]
            yield new_puzzle

# A* algorithm
def astar(start):
    heap = [(manhattan_distance(start), 0, start)]
    visited = {tuple(map(tuple, start))}
    while heap:
        _, cost, current = heapq.heappop(heap)
        if current == GOAL_STATE:
            return cost
        empty_i, empty_j = find_coord(current, 0)
        for move in generate_moves(current):
            if tuple(map(tuple, move)) not in visited:
                visited.add(tuple(map(tuple, move)))
                heapq.heappush(heap, (cost + manhattan_distance(move), cost + 1, move))
    return float('inf')

# Function to input a puzzle from the user
def input_puzzle():
    puzzle = []
    print("Enter the initial state of the 8-puzzle (Use 0 to represent the empty tile):")
    for i in range(3):
        row = input(f"Enter row {i+1} separated by spaces: ").split()
        row = [int(cell) for cell in row]
        puzzle.append(row)
    return puzzle

# Main function
def main():
    print("Welcome to the 8-puzzle solver!")
    initial_state = input_puzzle()
    print("Enter the goal state of the 8-puzzle (Use 0 to represent the empty tile):")
    goal_state = input_puzzle()
    moves = astar(initial_state)
    if moves != float('inf'):
        print(f"Minimum number of moves required to reach the goal state: {moves}")
    else:
        print("Goal state is not reachable from the initial state.")

if __name__ == "__main__":
    main()
