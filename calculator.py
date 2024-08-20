import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(0, 0)

expression = ""
input_text = tk.StringVar()

history = []

input_frame = tk.Frame(root, width=400, height=50, bd=0, bg="#1E1E1E")
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#1E1E1E", fg="white", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=8)  

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
       
        history.append(f"{expression} = {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_square_root():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_square():
    global expression
    try:
        result = str(float(expression)**2)
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_modulus():
    global expression
    try:
        result = str(eval(expression) % 100)
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_sin():
    global expression
    try:
        result = str(math.sin(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_cos():
    global expression
    try:
        result = str(math.cos(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_tan():
    global expression
    try:
        result = str(math.tan(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def btn_log():
    global expression
    try:
        result = str(math.log10(float(expression)))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("400x300")
    history_listbox = tk.Listbox(history_window, font=('arial', 12))
    history_listbox.pack(fill=tk.BOTH, expand=True)
    for item in history:
        history_listbox.insert(tk.END, item)

button_frame = tk.Frame(root, width=400, height=450, bg="#1E1E1E")
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '√',
    '1', '2', '3', '-', '^',
    '0', '.', '=', '+', '%',
    'sin', 'cos', 'tan', 'log', 'Hist'
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#FFA500", fg="white",
                        command=btn_equal, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "C":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_clear, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "√":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_square_root, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "^":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_square, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "%":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_modulus, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "sin":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_sin, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "cos":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_cos, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "tan":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_tan, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "log":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#696969", fg="white",
                        command=btn_log, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    elif button == "Hist":
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#FFA500", fg="white",
                        command=show_history, font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    else:
        btn = tk.Button(button_frame, text=button, width=5, height=2, bg="#333333", fg="white",
                        command=lambda x=button: btn_click(x), font=('arial', 14), relief=tk.FLAT, borderwidth=1)
    
    btn.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col == 5:
        col = 0
        row += 1

root.mainloop()
