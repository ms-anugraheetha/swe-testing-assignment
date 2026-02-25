import tkinter as tk
from calculator.quick_calc import QuickCalc

calc = QuickCalc()

current = ""

def press(value):
    global current
    current += str(value)
    display.set(current)

def clear():
    global current
    current = ""
    calc.clear()
    display.set("0")

def backspace():
    global current
    current = current[:-1]
    if current == "":
        display.set("0")
    else:
        display.set(current)

def calculate():
    global current
    try:
        result = eval(current)
        display.set(result)
        current = str(result)
    except ZeroDivisionError:
        display.set("Error")
        current = ""
    except:
        display.set("Invalid")
        current = ""

# Window setup
window = tk.Tk()
window.title("Quick-Calc")
window.geometry("320x420")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

display = tk.StringVar()
display.set("0")

entry = tk.Entry(
    window,
    textvariable=display,
    font=("Segoe UI", 24),
    justify="right",
    bd=0,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Button style function
def make_button(parent, text, command, bg="#3a3a3a"):
    return tk.Button(
        parent,
        text=text,
        font=("Segoe UI", 14),
        command=command,
        bg=bg,
        fg="white",
        bd=0,
        activebackground="#555"
    )

buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    frame = tk.Frame(window, bg="#1e1e1e")
    frame.pack(expand=True, fill="both", padx=10, pady=2)

    for btn in row:
        if btn == "=":
            action = calculate
            color = "#007acc"
        elif btn in "+-*/":
            action = lambda x=btn: press(x)
            color = "#ff9500"
        else:
            action = lambda x=btn: press(x)
            color = "#3a3a3a"

        make_button(frame, btn, action, color).pack(
            side="left", expand=True, fill="both", padx=2, pady=2
        )

# Bottom row for Clear and Backspace
bottom = tk.Frame(window, bg="#1e1e1e")
bottom.pack(expand=True, fill="both", padx=10, pady=5)

make_button(bottom, "Clear", clear, "#d9534f").pack(
    side="left", expand=True, fill="both", padx=2
)

make_button(bottom, "⌫", backspace, "#6c757d").pack(
    side="left", expand=True, fill="both", padx=2
)

window.mainloop()