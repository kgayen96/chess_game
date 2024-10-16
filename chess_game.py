import chess
import chess.engine

# Initialize a chess board
board = chess.Board()

# Set up the Stockfish engine (update this path to where Stockfish is installed on your machine)
engine = chess.engine.SimpleEngine.popen_uci("C:/Users/acer/stockfish")
def print_board():
    print(board)

def make_move(move):
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move! Please try again.")

def cpu_move():
    # CPU uses the engine to make the best move
    result = engine.play(board, chess.engine.Limit(time=2.0))
    board.push(result.move)

def main():
    print("Welcome to the Chess Game!")
    print_board()

    while not board.is_game_over():
        # Player's move
        move = input("Enter your move (e.g., e2e4): ")
        make_move(move)
        print_board()

        # CPU's move
        print("CPU is thinking...")
        cpu_move()
        print_board()

        if board.is_game_over():
            print("Game over!")
            break

if __name__ == "__main__":
    main()
