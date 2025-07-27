import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 10:
            raise ValueError("Password must be at least 10 characters long.")

        characters = list(string.ascii_lowercase)

        if uppercase_var.get():
            characters += list(string.ascii_uppercase)
        if digits_var.get():
            characters += list(string.digits)
        if symbols_var.get():
            characters += list(string.punctuation)

        if not characters:
            raise ValueError("Please select at least one character type!")

        password = []
        if uppercase_var.get():
            password.append(random.choice(string.ascii_uppercase))
        if digits_var.get():
            password.append(random.choice(string.digits))
        if symbols_var.get():
            password.append(random.choice(string.punctuation))

        password += random.choices(characters, k=length - len(password))
        random.shuffle(password)

        final_password = ''.join(password)
        password_label.config(text=final_password)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Function to copy to clipboard
def copy_to_clipboard():
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- GUI ----------------
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x400")
window.config(bg="#f0f8ff")

title_label = tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

# Password Length
tk.Label(window, text="Password Length:", font=("Arial", 12), bg="#f0f8ff").pack()
length_entry = tk.Entry(window, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

# Checkboxes
uppercase_var = tk.IntVar()
digits_var = tk.IntVar()
symbols_var = tk.IntVar()

tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var, bg="#f0f8ff").pack()
tk.Checkbutton(window, text="Include Numbers", variable=digits_var, bg="#f0f8ff").pack()
tk.Checkbutton(window, text="Include Symbols", variable=symbols_var, bg="#f0f8ff").pack()

# Generate Button
tk.Button(window, text="Generate Password", command=generate_password, bg="#4682b4", fg="white", font=("Arial", 12)).pack(pady=10)

# Output
password_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="green", bg="#f0f8ff")
password_label.pack(pady=10)

# Copy Button
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#32cd32", fg="white", font=("Arial", 11)).pack()

# Run GUI
window.mainloop()
