EMPTY = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = [[EMPTY for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def make_move(self, x, y, player):
        if self.board[x][y] == EMPTY:
            self.board[x][y] = player
            return True
        return False

    def undo_move(self, x, y):
        self.board[x][y] = EMPTY

    def is_full(self):
        return all(cell != EMPTY for row in self.board for cell in row)

    def get_available_moves(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.board[x][y] == EMPTY]

    def get_promising_moves(self):
        moves = set()
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != EMPTY:
                    for dx in range(-2, 3):
                        for dy in range(-2, 3):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == EMPTY:
                                moves.add((nx, ny))
        return list(moves) or self.get_available_moves()

    def check_winner(self, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != player:
                    continue
                for dx, dy in directions:
                    count = 0
                    for i in range(5):
                        nx, ny = x + dx * i, y + dy * i
                        if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player:
                            count += 1
                        else:
                            break
                    if count == 5:
                        return True
        return False

    def evaluate(self, player, opponent):
        score = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == EMPTY:
                    continue
                for dx, dy in directions:
                    player_count = 0
                    opponent_count = 0
                    empty_count = 0
                    for i in range(5):
                        nx, ny = x + dx * i, y + dy * i
                        if not (0 <= nx < self.size and 0 <= ny < self.size):
                            break
                        cell = self.board[nx][ny]
                        if cell == player:
                            player_count += 1
                        elif cell == opponent:
                            opponent_count += 1
                        else:
                            empty_count += 1
                    if opponent_count == 0 and player_count > 0 and player_count + empty_count >= 5:
                        if player_count == 4:
                            score += 1000
                        elif player_count == 3:
                            score += 100
                        elif player_count == 2:
                            score += 10
                    if player_count == 0 and opponent_count > 0 and opponent_count + empty_count >= 5:
                        if opponent_count == 4:
                            score -= 1000
                        elif opponent_count == 3:
                            score -= 100
                        elif opponent_count == 2:
                            score -= 10
        return score