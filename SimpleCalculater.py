import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# Function to update the entry widget
def button_click(item):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + item)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character
def delete_last():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the window
row_value = 1
col_value = 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, width=4, height=2, font=('Arial', 18), command=lambda: evaluate_expression(entry.get()))
    else:
        button = tk.Button(root, text=button_text, width=4, height=2, font=('Arial', 18), command=lambda text=button_text: button_click(text))
    
    button.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Add clear and delete buttons
clear_button = tk.Button(root, text='C', width=4, height=2, font=('Arial', 18), command=clear_entry)
clear_button.grid(row=row_value, column=0)

delete_button = tk.Button(root, text='Del', width=4, height=2, font=('Arial', 18), command=delete_last)
delete_button.grid(row=row_value, column=1)

# Start the main loop
root.mainloop()
