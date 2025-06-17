from tkinter import*

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")
    except:
        show_error()

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")
    except:
        show_error()

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")
    except:
        show_error()

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result = float(entry1.get()) / num2
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")
    except:
        show_error()

def show_error():
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, "Error")
    entry_result.config(state="readonly")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

label_title = tk.Label(root, text="Calculator", font=("Arial", 16))
label_title.pack()

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

bt_add = tk.Button(root, text="Add", width=10, command=add)
bt_add.pack()

bt_sub = tk.Button(root, text="Subtract", width=10, command=subtract)
bt_sub.pack()

bt_mul = tk.Button(root, text="Multiply", width=10, command=multiply)
bt_mul.pack()

bt_div = tk.Button(root, text="Divide", width=10, command=divide)
bt_div.pack()

root.mainloop()
