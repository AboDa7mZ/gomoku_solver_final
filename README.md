Gomoku AI Solver 🎮🧠
A Python-based AI Gomoku (Five-in-a-Row) game that allows:

A Human vs AI mode using the Minimax algorithm

An AI vs AI mode where Minimax plays against Alpha-Beta Pruning

📌 Game Overview
Gomoku is a two-player abstract strategy board game. Players alternate turns placing a stone of their color on an empty cell of the board. The objective is simple:
Get five stones in a row (horizontally, vertically, or diagonally) before your opponent does.

This project simulates and solves Gomoku using classic search algorithms:

Minimax Algorithm

Alpha-Beta Pruning

🧩 Project Structure
✅ Game Modes:
Human vs AI: You play against the AI that uses Minimax to make decisions.

AI vs AI: The two algorithms (Minimax vs Alpha-Beta Pruning) play against each other automatically.

🛠️ Components
🎮 Game Engine
Manages the Gomoku board state.

Uses search algorithms to find optimal moves.

Applies depth-limited search to control performance.

Displays updated board after every move.

🤖 AI Algorithms
Minimax: Basic decision-making algorithm.

Alpha-Beta Pruning: An optimized version of Minimax to reduce computation time.

📚 Project Knowledge Base
Gomoku Rules and Board Representation

Minimax Algorithm (Decision Trees)

Alpha-Beta Pruning (Efficiency Optimization)

⌨️ Input
Initial (or current) board state.

Player input (in Human vs AI mode).

🖥️ Output
AI’s chosen move (row, column coordinates).

Updated board printed after each move.

🧪 Grading Criteria
Feature	Points
User Input Handling	1
Game State Representation	2
Game Engine (Rules & Move Generation)	2
Formatted Output (Move Coordinates)	1
AI: Minimax Implementation	2
AI: Alpha-Beta Pruning Implementation	2
AI vs AI Mode	2
Bonus: GUI (e.g., using Tkinter)	2

💡 Bonus Feature: GUI
A brilliant graphical user interface (built with Tkinter) makes it easy to:

Visualize moves

Interact with the game board

Switch between game modes

🚀 Getting Started
bash
Copy
Edit

# Run the game
python main.py
For the GUI version, ensure you have tkinter installed and run gui.py instead.

📎 Notes
Default board size: 15x15 (can be modified)

Depth limit configurable for AI performance tuning

Board input format: list of lists or user-friendly console interface

📤 Contributions
Feel free to fork and improve! Whether it’s enhancing the GUI, optimizing search heuristics, or extending to multiplayer – contributions are welcome.

📧 Contact
Abdulrahman Zakaria
📧 abdulrahman.aboda7m@hotmail.com


