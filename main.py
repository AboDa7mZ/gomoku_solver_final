from board import Board, PLAYER_X, PLAYER_O
from minimax import minimax

def human_vs_ai():
    board = Board()
    player = PLAYER_X
    ai = PLAYER_O
    turn = PLAYER_X

    while True:
        board.display()
        if turn == player:
            x, y = map(int, input("Enter your move (row col): ").split())
            if not board.make_move(x, y, player):
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            _, move = minimax(board, 2, True, ai, player)
            if move:
                board.make_move(*move, ai)

        if board.check_winner(turn):
            board.display()
            print(f"{turn} wins!")
            break
        if board.is_full():
            board.display()
            print("It's a draw!")
            break
        turn = PLAYER_O if turn == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    human_vs_ai()