humanMark="X"
aiMark="O"

def isCellEmpty(board, i, j):
    return (board[i][j] == "")

def check_winner(board, mark):
    for i in range(len(board)):
        if(board[i][0] == board[i][1] == board[i][2] == mark):
            return True
        if(board[0][i] == board[1][i] == board[2][i] == mark):
            return True
    if(board[0][0] == board[1][1] == board[2][2] == mark):
        return True
    if(board[0][2] == board[1][1] == board[2][0] == mark):
        return True
    return False

def check_draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == ""):
                return False
    return True


def miniMax(board, depth, isMaximizing):
    if(check_winner(board, humanMark)):
        return -1
    elif(check_winner(board, aiMark)):
        return 1
    elif(check_draw(board)):
        return 0
    
    if(isMaximizing):
        score = -10000
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(isCellEmpty(board, i, j)):
                    board[i][j] = aiMark
                    score = max(miniMax(board, depth+1, False), score)
                    board[i][j] = ""
        return score
    score = 1000
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(isCellEmpty(board, i, j)):
                board[i][j] = humanMark
                score = min(miniMax(board, depth+1, True), score)
                board[i][j] = ""
    return score

def findBestMove(board):
    bestVal=-1000
    bestMove = (-1, -1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(isCellEmpty(board, i, j)):
                board[i][j] = aiMark
                moveVal = miniMax(board, 0, False)
                board[i][j] = ""
                if(moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def main():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    printBoard(board)
    while(True):
        print("Enter the position where you want to place your mark")
        x = int(input("Enter the row: "))
        y = int(input("Enter the column: "))
        if(isCellEmpty(board, x, y)):
            board[x][y] = humanMark
            printBoard(board)
            if(check_winner(board, humanMark)):
                print("You won")
                break
            if(check_draw(board)):
                print("It's a draw")
                break
            move = findBestMove(board)
            board[move[0]][move[1]] = aiMark
            printBoard(board)
            if(check_winner(board, aiMark)):
                print("AI won")
                break
            if(check_draw(board)):
                print("It's a draw")
                break
        else:
            print("Cell is not empty")

if(__name__ == "__main__"):
    main()