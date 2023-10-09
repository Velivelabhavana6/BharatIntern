import tkinter as tk
from tkinter import font

# Function to perform calculations
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append button text to the input field
def append_text(button_text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + button_text)

# Function to clear the input field
def clear_input():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Set the initial window size

# Create an input field
entry_font = font.nametofont("TkDefaultFont")
entry_font.configure(size=36)
entry = tk.Entry(root, width=20, font=entry_font, justify="right", bd=15)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
entry.config(bg="lightgray")

# Define button colors
button_bg = "lightgray"
button_fg = "black"
button_borderwidth = 1

# Create calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  # Clear button
]

button_font = font.nametofont("TkDefaultFont")
button_font.configure(size=24)

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == 'C':
        tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=20,
            font=button_font,
            bg="lightcoral",
            fg="white",
            bd=button_borderwidth,
            command=clear_input
        ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    elif button_text == '=':
        tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=20,
            font=button_font,
            bg="dodgerblue",
            fg="white",
            bd=button_borderwidth,
            command=evaluate_expression
        ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=20,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
            bd=button_borderwidth,
            command=lambda btn=button_text: append_text(btn)
        ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure column and row weights for even distribution
for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i + 1, weight=1)

# Run the GUI
root.mainloop()
