def display_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

def check_winner(board, player):
    return any(
        all(cell == player for cell in row) or
        all(board[i][col] == player for i in range(3))
        for col, row in enumerate(board)
        ) or all(
            board[i][i] == player
            for i in range(3)
        ) or all(
            board[i][2 - i] == player
            for i in range(3)
        )

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing, ai, human):
    if check_winner(board, ai):
        return 1
    if check_winner(board, human):
        return -1
    if is_full(board):
        return 0

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai if is_maximizing else human
                score = minimax(board, not is_maximizing, ai, human)
                board[i][j] = " "
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

def find_best_move(board, ai, human):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                score = minimax(board, False, ai, human)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    ai, human = "O", "X"

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        # Human move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = human
                    break
                print("Cell is occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Use two numbers (0-2).")

        display_board(board)
        if check_winner(board, human):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI's turn...")
        ai_move = find_best_move(board, ai, human)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = ai

        display_board(board)
        if check_winner(board, ai):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a tie!")
            break

play_game()
