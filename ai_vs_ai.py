from board import Board, PLAYER_X, PLAYER_O
from minimax import minimax
from alphabeta import alphabeta

def ai_vs_ai():
    board = Board()
    turn = PLAYER_X

    while True:
        board.display()
        algo_name = "Minimax" if turn == PLAYER_X else "Alpha-Beta"
        print(f"AI ({algo_name})'s turn")
        if turn == PLAYER_X:
            _, move = minimax(board, 3, True, PLAYER_X, PLAYER_O)
        else:
            _, move = alphabeta(board, 3, float('-inf'), float('inf'), True, PLAYER_O, PLAYER_X)

        if move:
            board.make_move(*move, turn)

        if board.check_winner(turn):
            board.display()
            print(f"AI ({algo_name}) wins!")
            break
        if board.is_full():
            board.display()
            print("It's a draw!")
            break

        turn = PLAYER_O if turn == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    ai_vs_ai()