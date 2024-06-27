import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = 'O'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        move = input("Enter your move (row and column): ").split()
        row, col = int(move[0]), int(move[1])
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        if check_full(board):
            print("It's a draw!")
            break

        ai_move(board)
        print("AI move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if check_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
