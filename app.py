from flask import Flask, jsonify
import chess
import chess.engine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the chess board
board = chess.Board()

# Set up the Stockfish engine (update with your Stockfish engine path)
engine = chess.engine.SimpleEngine.popen_uci("C:/Users/acer/Chess_project/stockfish/stockfish-windows-x86-64-avx2.exe")

@app.route('/favicon.ico')
def favicon():
    return "", 204  # Returning an empty response with status 204 (No Content)

@app.route('/cpu_vs_cpu', methods=['POST'])
def cpu_vs_cpu():
    while not board.is_game_over():
        # CPU 1 (white) move
        result_white = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result_white.move)
        if board.is_game_over():
            break

        # CPU 2 (black) move
        result_black = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result_black.move)

    return jsonify({"board": board.fen(), "result": "Game over!" if board.is_game_over() else "In progress"})


if __name__ == '__main__':
    app.run(debug=True)
