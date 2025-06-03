import tkinter as tk
from tkinter import messagebox

# Create main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for winner or draw
def check_winner():
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# Button click handler
def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global board, current_player
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Create 3x3 grid of buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 32), width=5, height=2,
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Run the GUI loop
root.mainloop()
