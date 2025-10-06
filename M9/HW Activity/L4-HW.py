import tkinter as tk
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))  
    password_var.set(password)

root = tk.Tk()
root.title("Easy Password Generator")
root.geometry("300x180")

label = tk.Label(root, text="Click to Generate Password", font=("Arial", 12))
label.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=25, justify="center")
password_entry.pack(pady=10)

root.mainloop()
