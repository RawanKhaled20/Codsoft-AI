"""Author: Rawan Khaled https://github.com/RawanKhaled20/Codsoft-AI.git"""

def evaluate(board):
    # Checking rows for a win or loss
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10
    # Checking columns for a win or loss
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    # Checking main diagonal for a win or loss
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    # Checking the other diagonal for a win or loss
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # If no one wins
    return 0

def minmax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not any('-' in row for row in board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, minmax(board, depth + 1, not is_max))
                    board[i][j] = '-'
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minmax(board, depth + 1, not is_max))
                    board[i][j] = '-'
        return best
def minmax_alphabeta(board, depth, is_max,alpha,beta):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not any('-' in row for row in board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, minmax_alphabeta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = '-'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minmax_alphabeta(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = '-'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board,choice):
    best_val = -1000
    best_move = (-1, -1)
    alpha=-1000
    beta=1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                if choice==1:
                  move_val = minmax(board, 0, False)
                  board[i][j] = '-'
                else:
                    move_val=minmax_alphabeta(board,0,False,alpha,beta)
                    board[i][j] = '-'

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# To add spaces between each _ in a row for a better user interface
def print_board(board):
    for row in board:
        print(' '.join(row))

def main():
    board = [['-' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    print("1.MinMax")
    print("2.MinMax with alpha beta pruning")
    choice=int(input("Enter 1 or 2 to play with an AI MinMax user or AI with MinMax and aplpha beta pruning user"))
    print()

    #Taking human player move (O)
    while True:
        #Remember to add a space between the values you enter
        x, y = map(int, input("Enter your move (row col): ").split())
        if board[x][y] != '-':
            print("Invalid move. Try again.")
            continue

        board[x][y] = 'O'
        print_board(board)

        # 3 Os determined
        if evaluate(board) == -10:
            print("You win!")
            break
        #Check if there is a tie after each move
        if not any('-' in row for row in board):
            print("It's a draw!")
            break
        #Creating AI move using MinMax (X)
        ai_x, ai_y = find_best_move(board,choice)
        board[ai_x][ai_y] = 'X'
        print("AI's move:")
        print_board(board)
        # 3 Xs determined
        if evaluate(board) == 10:
            print("AI wins!")
            break
        #Check if there is a tie after each move
        if not any('-' in row for row in board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()