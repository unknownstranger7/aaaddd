import math

X = 'X'
O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if the game is over
def game_over(board):
    return not any(EMPTY in row for row in board)

# Function to evaluate the board
def evaluate(board):
    # Check rows, columns, and diagonals for winning conditions
    for row in board:
        if all([cell == row[0] for cell in row]) and row[0] != EMPTY:
            return row[0]

    for col in range(3):
        if all([board[row][col] == board[0][col] for row in range(3)]) and board[0][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # Check for draw
    if game_over(board):
        return 'draw'

    return None

# Function to get empty cells
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    if result is not None:
        if result == X:
            return -10 + depth
        elif result == O:
            return 10 - depth
        else:
            return 0

    if is_maximizing:
        best_score = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = O
            score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = X
            score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Function to find the best move
def best_move(board):
    best_score = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = O
        score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    while True:
        print_board(board)
        if game_over(board):
            result = evaluate(board)
            if result == 'draw':
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break
        player_move = input("Enter your move (row and column separated by space): ")
        row, col = map(int, player_move.split())
        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[row][col] = X
        if game_over(board):
            result = evaluate(board)
            if result == 'draw':
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break
        print("Computer's move:")
        comp_row, comp_col = best_move(board)
        board[comp_row][comp_col] = O

# Play the game
play_game()
