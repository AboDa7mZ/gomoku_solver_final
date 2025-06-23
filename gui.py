import tkinter as tk
import threading
from board import Board, PLAYER_X, PLAYER_O
from minimax import minimax
from alphabeta import alphabeta

CELL_SIZE = 40
BOARD_SIZE = 15

class GomokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku - Five in a Row")
        self.mode = tk.StringVar(value="Human vs AI")
        self.algorithm = tk.StringVar(value="Minimax")
        self.thinking_dots = 0
        self.setup_ui()
        self.new_game()

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.configure(bg="#2c3e50")

        control_frame = tk.Frame(self.main_frame, bg="#34495e", pady=10)
        control_frame.pack(fill="x")

        tk.Label(control_frame, text="Mode:", bg="#34495e", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.OptionMenu(control_frame, self.mode, "Human vs AI", "AI vs AI").pack(side=tk.LEFT, padx=5)

        tk.Label(control_frame, text="AI Algorithm:", bg="#34495e", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.OptionMenu(control_frame, self.algorithm, "Minimax", "Alpha-Beta").pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="New Game", command=self.new_game, bg="#3498db", fg="white", font=("Arial", 12, "bold"), relief="flat").pack(side=tk.LEFT, padx=5)

        self.status_var = tk.StringVar(value="Player X's Turn")
        tk.Label(self.main_frame, textvariable=self.status_var, bg="#2c3e50", fg="white", font=("Arial", 14, "bold")).pack(pady=10)

        self.canvas = tk.Canvas(self.main_frame, width=BOARD_SIZE*CELL_SIZE, height=BOARD_SIZE*CELL_SIZE, bg="#d2b48c")
        self.canvas.pack(pady=20)
        self.canvas.bind("<Button-1>", self.on_click)

    def new_game(self):
        self.board = Board(BOARD_SIZE)
        self.turn = PLAYER_X
        self.canvas.delete("all")
        self.draw_grid()
        self.status_var.set(f"Player {self.turn}'s Turn")
        self.thinking_dots = 0
        if self.mode.get() == "AI vs AI":
            self.root.after(500, self.ai_vs_ai)

    def draw_grid(self):
        for i in range(BOARD_SIZE):
            self.canvas.create_line(0, i*CELL_SIZE, BOARD_SIZE*CELL_SIZE, i*CELL_SIZE, fill="#8b4513", width=2)
            self.canvas.create_line(i*CELL_SIZE, 0, i*CELL_SIZE, BOARD_SIZE*CELL_SIZE, fill="#8b4513", width=2)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.canvas.create_oval(i*CELL_SIZE-3, j*CELL_SIZE-3, i*CELL_SIZE+3, j*CELL_SIZE+3, fill="#8b4513")

    def draw_move(self, x, y, player):
        px = y * CELL_SIZE + CELL_SIZE//2
        py = x * CELL_SIZE + CELL_SIZE//2
        color = "black" if player == PLAYER_X else "white"
        shadow_color = "#555555" if player == PLAYER_X else "#aaaaaa"
        self.canvas.create_oval(px-12, py-12, px+12, py+12, fill=shadow_color)
        self.canvas.create_oval(px-10, py-10, px+10, py+10, fill=color, outline="#333333")

    def on_click(self, event):
        if self.mode.get() != "Human vs AI" or self.turn != PLAYER_X:
            return
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if self.board.make_move(row, col, self.turn):
            self.draw_move(row, col, self.turn)
            if self.check_end(self.turn):
                return
            self.turn = PLAYER_O
            self.thinking_dots = 0
            self.update_thinking_status()
            threading.Thread(target=self.ai_move, daemon=True).start()

    def update_thinking_status(self):
        if self.turn == PLAYER_O and not self.check_end(self.turn):
            self.thinking_dots = (self.thinking_dots + 1) % 4
            dots = "." * self.thinking_dots
            self.status_var.set(f"AI's Turn (Thinking{dots})")
            self.root.after(500, self.update_thinking_status)

    def ai_move(self):
        algo = minimax if self.algorithm.get() == "Minimax" else alphabeta
        args = [self.board, 2, True, PLAYER_O, PLAYER_X]
        if algo == alphabeta:
            args.insert(2, float('-inf'))
            args.insert(3, float('inf'))
        _, move = algo(*args)
        self.root.after(0, self.update_after_ai_move, move)

    def update_after_ai_move(self, move):
        if move:
            self.board.make_move(*move, PLAYER_O)
            self.draw_move(*move, PLAYER_O)
            if self.check_end(PLAYER_O):
                return
            self.turn = PLAYER_X
            self.status_var.set("Player X's Turn")

    def ai_vs_ai(self):
        if self.mode.get() != "AI vs AI":
            return
        current_player = self.turn
        opponent = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        algo = minimax if current_player == PLAYER_X else alphabeta
        algo_name = "Minimax" if current_player == PLAYER_X else "Alpha-Beta"
        self.thinking_dots = 0
        self.status_var.set(f"AI ({algo_name})'s Turn")
        self.update_thinking_status()
        threading.Thread(target=self.ai_vs_ai_move, args=(current_player, opponent, algo, algo_name), daemon=True).start()

    def ai_vs_ai_move(self, current_player, opponent, algo, algo_name):
        args = [self.board, 2, True, current_player, opponent]
        if algo == alphabeta:
            args.insert(2, float('-inf'))
            args.insert(3, float('inf'))
        _, move = algo(*args)
        self.root.after(0, self.update_after_ai_vs_ai_move, move, current_player, opponent)

    def update_after_ai_vs_ai_move(self, move, current_player, opponent):
        if move:
            self.board.make_move(*move, current_player)
            self.draw_move(*move, current_player)
            if self.check_end(current_player):
                return
            self.turn = opponent
            self.root.after(500, self.ai_vs_ai)

    def check_end(self, player):
        if self.board.check_winner(player):
            self.canvas.unbind("<Button-1>")
            winner = "Player X" if player == PLAYER_X else f"AI ({self.algorithm.get()})"
            self.status_var.set(f"{winner} Wins!")
            self.canvas.create_text(BOARD_SIZE*CELL_SIZE//2, BOARD_SIZE*CELL_SIZE//2, text=f"{winner} Wins!", font=("Arial", 24, "bold"), fill="green")
            return True
        if self.board.is_full():
            self.status_var.set("It's a Draw!")
            self.canvas.create_text(BOARD_SIZE*CELL_SIZE//2, BOARD_SIZE*CELL_SIZE//2, text="It's a Draw!", font=("Arial", 24, "bold"), fill="blue")
            return True
        return False

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg="#2c3e50")
    game = GomokuSy = GomokuGUI(root)
    root.mainloop()