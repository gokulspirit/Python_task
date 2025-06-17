import tkinter as tk

# --- Functions for operations ---
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        display_result(result)
    except:
        display_error()

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        display_result(result)
    except:
        display_error()

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        display_result(result)
    except:
        display_error()

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
        display_result(result)
    except:
        display_error()

# --- Display result in entry box ---
def display_result(value):
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, str(round(value, 2)))
    entry_result.config(state="readonly")

# --- Display error message ---
def display_error():
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, "Error")
    entry_result.config(state="readonly")

# --- GUI Setup ---
root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

label_title = tk.Label(root, text="Calculator", font=("Arial", 16))
label_title.pack(pady=5)

label_num1 = tk.Label(root, text="Number 1:")
label_num1.pack()
entry1 = tk.Entry(root, bd=1)
entry1.pack()

label_num2 = tk.Label(root, text="Number 2:")
label_num2.pack()
entry2 = tk.Entry(root, bd=1)
entry2.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()
entry_result = tk.Entry(root, bd=1, state="readonly")
entry_result.pack()

# --- Buttons for operations ---
bt_add = tk.Button(root, text="Add", width=10, command=add)
bt_add.pack(pady=2)

bt_sub = tk.Button(root, text="Subtract", width=10, command=subtract)
bt_sub.pack(pady=2)

bt_mul = tk.Button(root, text="Multiply", width=10, command=multiply)
bt_mul.pack(pady=2)

bt_div = tk.Button(root, text="Divide", width=10, command=divide)
bt_div.pack(pady=2)

# --- Run the application ---
root.mainloop()
