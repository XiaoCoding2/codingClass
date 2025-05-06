
import random

def print_board(board):
  """Prints the current state of the Tic-Tac-Toe board."""
  print("-------------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} |", end="")
    print("\n-------------")

def check_win(board):
  """Checks if a player has won."""
  # Check rows
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]

  # Check columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return board[0][col]

  # Check diagonals
  if (board[0][0] == board[1][1] == board[2][2] or 
      board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
    return board[1][1]

  return None

def check_draw(board):
  """Checks if the game is a draw."""
  for row in board:
    for cell in row:
      if cell == " ":
        return False
  return True

def get_empty_cells(board):
  """Returns a list of empty cells on the board."""
  empty_cells = []
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        empty_cells.append((row, col))
  return empty_cells

def ai_move(board):
  """Determines the AI's move using a simple strategy."""
  # Prioritize winning moves
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        board[row][col] = "O"
        if check_win(board) == "O":
          return row, col
        board[row][col] = " "

  # Prioritize blocking opponent's winning moves
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        board[row][col] = "X"
        if check_win(board) == "X":
          board[row][col] = "O"
          return row, col
        board[row][col] = " "

  # Choose a random empty cell
  empty_cells = get_empty_cells(board)
  if empty_cells:
    row, col = random.choice(empty_cells)
    return row, col

  return row,col
def play_game():
  """Plays a game of Tic-Tac-Toe."""
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    print_board(board)

    if current_player == "X":
      row, col = map(int, input("Enter your move (row, col): ").split(","))
      row -= 1  # Adjust for 0-based indexing
      col -= 1
    else:
      print("AI's turn:")
      row, col = ai_move(board)

    if (row < 0)or(row > 2)or(col < 0)or(col > 2)or(board[row][col] != " "):
      print("Invalid move. Try again.")
      continue

    board[row][col] = current_player

    winner = check_win(board)
    if winner:
      print_board(board)
      print(f"{winner} wins!")
      break

    if check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()