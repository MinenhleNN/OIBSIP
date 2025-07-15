import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# GUI setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)

# Title
tk.Label(window, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Length input 
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window, justify='center')
length_entry.insert(0, "12")
length_entry.pack()

# Character checkboxes
var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Include Lowercase (a-z)", variable=var_lower).pack()
tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=var_upper).pack()
tk.Checkbutton(window, text="Include Digits (0-9)", variable=var_digits).pack()
tk.Checkbutton(window, text="Include Symbols (!@#)", variable=var_symbols).pack()

# Result
result_entry = tk.Entry(window, font=("Helvetica", 12), justify='center')
result_entry.pack(pady=5)

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number.")
        return
    
    if length < 6:
        messagebox.showwarning("Weak Password", "Use at least 6 characters for a secure password.")
        return
    
    # Build character pool
    char_pool = ''
    if var_lower.get():
        char_pool += string.ascii_lowercase
    if var_upper.get():
        char_pool += string.ascii_uppercase
    if var_digits.get():
        char_pool += string.digits
    if var_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Copy to clipboard
def copy_to_clipboard():
    pyperclip.copy(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Buttons
tk.Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

# Run the GUI loop
window.mainloop()