def minimax(board, depth, maximizing_player, player, opponent):
    if board.check_winner(player):
        return 10000, None
    if board.check_winner(opponent):
        return -10000, None
    if depth == 0 or board.is_full():
        return board.evaluate(player, opponent), None

    best_move = None
    if maximizing_player:
        best_score = float('-inf')
        for move in board.get_promising_moves():
            board.make_move(*move, player)
            score, _ = minimax(board, depth-1, False, player, opponent)
            board.undo_move(*move)
            if score > best_score:
                best_score = score
                best_move = move
    else:
        best_score = float('inf')
        for move in board.get_promising_moves():
            board.make_move(*move, opponent)
            score, _ = minimax(board, depth-1, True, player, opponent)
            board.undo_move(*move)
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move