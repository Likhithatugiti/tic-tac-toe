def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, mark):
    for row in board:
        if row.count(mark) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(mark) == 3:
            return True
    if [board[i][i] for i in range(3)].count(mark) == 3 or [board[i][2-i] for i in range(3)].count(mark) == 3:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while " " in [cell for row in board for cell in row]:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken, try again.")

    print_board(board)
    print("It's a tie!")

