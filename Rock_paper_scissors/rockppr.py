import tkinter as tk
import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Function to determine winner
def play(player_choice):
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(
        text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}"
    )

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock"))
paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper"))
scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
