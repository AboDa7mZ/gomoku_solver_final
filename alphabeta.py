def alphabeta(board, depth, alpha, beta, maximizing_player, player, opponent):
    if board.check_winner(player):
        return 10000, None
    if board.check_winner(opponent):
        return -10000, None
    if depth == 0 or board.is_full():
        return board.evaluate(player, opponent), None

    best_move = None
    if maximizing_player:
        value = float('-inf')
        for move in board.get_promising_moves():
            board.make_move(*move, player)
            score, _ = alphabeta(board, depth-1, alpha, beta, False, player, opponent)
            board.undo_move(*move)
            if score > value:
                value = score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = float('inf')
        for move in board.get_promising_moves():
            board.make_move(*move, opponent)
            score, _ = alphabeta(board, depth-1, alpha, beta, True, player, opponent)
            board.undo_move(*move)
            if score < value:
                value = score
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move