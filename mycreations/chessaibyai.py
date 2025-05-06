
import pygame
import chess

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
FPS = 60
FONT = pygame.font.Font(None, 36)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess with AI")
clock = pygame.time.Clock()

# Piece values for evaluation
PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # King's value is considered infinite in practical terms
}

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)
    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Evaluate board function
def evaluate_board(board):
    if board.is_checkmate():
        return float('inf') if board.turn else float('-inf')
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    eval = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            eval += value if piece.color == chess.WHITE else -value
    return eval

# Find the best move using minimax
def find_best_move(board, depth):
    best_move = None
    best_value = float('-inf') if board.turn else float('inf')

    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, float('-inf'), float('inf'), not board.turn)
        board.pop()

        if board.turn and board_value > best_value:
            best_value = board_value
            best_move = move
        elif not board.turn and board_value < best_value:
            best_value = board_value
            best_move = move

    return best_move

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(board):
    piece_images = {}
    for piece in chess.PIECE_SYMBOLS[1:]:
        for color in [True, False]:
            key = (piece.upper() if color else piece)
            piece_images[key] = pygame.transform.scale(
                pygame.image.load(f"assets/{key}.png"), (SQUARE_SIZE, SQUARE_SIZE))
    
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = square % 8
            row = 7 - (square // 8)
            screen.blit(piece_images[piece.symbol()], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square_under_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARE_SIZE
    row = 7 - (mouse_y // SQUARE_SIZE)
    return chess.square(col, row)

def main():
    running = True
    board = chess.Board()
    selected_square = None
    move_made = False

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_under_mouse()
                if selected_square is None:
                    if board.piece_at(square) and board.color_at(square) == chess.WHITE:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        move_made = True
                    selected_square = None

        if move_made:
            move_made = False
            best_move = find_best_move(board, 3)  # AI depth
            if best_move:
                board.push(best_move)

        # Draw the board and pieces
        draw_board()
        draw_pieces(board)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
