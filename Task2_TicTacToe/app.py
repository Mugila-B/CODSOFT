import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i] == player for i in combo) for combo in win_conditions)

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(score, best)
        return best

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    move = int(input("Enter position (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move")
        player_move()

while True:
    print_board()
    player_move()

    if check_winner(board, "X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print("Draw!")
        break

    ai_move()

    if check_winner(board, "O"):
        print_board()
        print("AI wins!")
        break

    if is_draw():
        print("Draw!")
        break
