# EXP3: 8 Puzzle problem using AStar Algorithm
# Name: Smit Sutariya



# Define a class for individual nodes in the puzzle
class Node:
    def __init__(self, data, level, fval):
        self.data = data  # Puzzle configuration
        self.level = level  # Level in the search tree
        self.fval = fval  # F-value (evaluation function)
        

    # This method creates child nodes by moving the empty cell (represented by '_') in different directions.
    # It finds the current position (x, y) of the empty cell in the puzzle grid.
    def generate_child(self):
        x, y = self.find(self.data, '_')  # Find the position of the empty cell
        # Define the possible moves for the empty cell: left, right, up, and down.
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []  # List to store generated child nodes
        # Iterate over each possible move.
        for i in val_list:
            # Try to move the empty cell to the new position (i[0], i[1]).
            child = self.shuffle(self.data, x, y, i[0], i[1])
            # If the move is valid (i.e., the new position is within the puzzle boundaries),
            # create a new node representing the resulting puzzle configuration.
            if child is not None:
                # Create a new Node object representing the child node.
                # Increment the level of the child node by 1 compared to the current node.
                # Initially, the f-value of the child node is set to 0 and will be updated later.
                child_node = Node(child, self.level + 1, 0)
                # Add the child node to the list of children.
                children.append(child_node)
        # Return the list of generated child nodes.
        return children
    

    # Move the empty cell in the puzzle to a new position specified by (x2, y2).
    # The method checks if the new position is within the puzzle boundaries before performing the move.
    def shuffle(self, puz, x1, y1, x2, y2):
        # Check if the new position (x2, y2) is within the boundaries of the puzzle grid.
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            # Create a copy of the puzzle configuration to avoid modifying the original puzzle.
            temp_puz = self.copy(puz)
            # Swap the values of the cells at positions (x1, y1) and (x2, y2) to move the empty cell.
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            # Return the new puzzle configuration after the move.
            return temp_puz
        else:
            # If the new position is outside the puzzle boundaries, return None.
            return None


    # This method creates a new copy of the given puzzle configuration to avoid modifying the original puzzle.
    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp


    # This method searches for the position (row, column) of a specified value in the puzzle configuration.
    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

# Define a class for the puzzle solving process
class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []  # List of open nodes
        self.closed = []  # List of closed nodes
        

    # This method prompts the user to input the initial puzzle configuration.
    # It reads the input row by row, splitting the elements by space to form a 2D list representing the puzzle grid.
    def accept(self):
        puz = []  
        for i in range(0, self.n):
            # Prompt the user to input a row of the puzzle configuration.
            temp = input().split(" ")
            # Append the input row to the list representing the puzzle grid.
            puz.append(temp)
        # Return the 2D list representing the puzzle configuration.
        return puz
    

    # Evaluation function f(x) = h(x) + g(x)
    # It combines the heuristic function h(x) (number of misplaced tiles) with the level of the node in the search tree.
    def f(self, start, goal):
        # Calculate the heuristic value h(x) by comparing the current puzzle configuration with the goal configuration.
        # Add the level of the current node to the heuristic value to calculate f(x).
        return self.h(start.data, goal) + start.level
    

    # Heuristic function (number of misplaced tiles)
    # It counts the number of tiles that are misplaced in the current configuration compared to the goal configuration.
    def h(self, start, goal):
        temp = 0 
        for i in range(0, self.n):
            for j in range(0, self.n):
                # Check if the tile in the current position is not empty ('_') and is misplaced.
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    # If the tile is misplaced, increment the heuristic value.
                    temp += 1
        return temp
    
    
    # This method checks whether a given puzzle configuration is solvable or not.
    def is_solvable(self, puzzle):
        inversions = 0  
        # Flatten the puzzle grid into a 1D list and remove the empty cell ('_').
        flatten_puzzle = [item for sublist in puzzle for item in sublist if item != '_']
        
        for i in range(len(flatten_puzzle)):
            for j in range(i + 1, len(flatten_puzzle)):
                # If the current tile is greater than a tile that comes after it, it is considered an inversion.
                if flatten_puzzle[i] > flatten_puzzle[j]:
                    inversions += 1
        # Find the row index of the empty cell ('_') in the puzzle grid.
        blank_row = Node(puzzle, 0, 0).find(puzzle, '_')[0]
        # Check if the sum of inversions and the row index of the empty cell is even.
        # If the sum is even, the puzzle is solvable; otherwise, it is not solvable.
        return (inversions + blank_row) % 2 == 0


    # Main process for solving the puzzle
    def process(self):
        # Accept start and goal puzzle configurations
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")
        goal = self.accept()

        # Check if the puzzle is solvable
        if not self.is_solvable(start):
            print("The puzzle is not solvable. Exiting.")
            return

        # Initialize the start node with the start state matrix and calculate its f-value.
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        # Add the start node to the open list.
        self.open.append(start)

        print("\n\n")

        # Iterate until the goal state is reached.
        while True:
            cur = self.open[0] 
            # Print the current state matrix.
            print("==================================================\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            # Check if the current state matrix matches the goal state matrix.
            if self.h(cur.data, goal) == 0:
                break  # If the goal state is reached, exit the loop.

            # Generate child nodes for the current node.
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            # Move the current node from the open list to the closed list.
            self.closed.append(cur)
            del self.open[0]  # Remove the current node from the open list.
            self.open.sort(key=lambda x: x.fval, reverse=False)  # Sort the open list based on f-value.

# Create a Puzzle object with size 3x3 and start the solving process
puz = Puzzle(3)
puz.process()
