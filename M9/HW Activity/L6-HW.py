import tkinter as tk
import random

def play(user):
    computer = random.choice(["Rock", "Paper", "Scissors"])
    if user == computer:
        result = "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"You: {user}\nComputer: {computer}\n{result}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("250x300")

tk.Label(root, text="Choose:").pack(pady=5)

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=5)

result_label = tk.Label(root, text="", pady=20)
result_label.pack()

root.mainloop()
