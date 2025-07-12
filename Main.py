from tkinter import *
import math

expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        # Evaluate using math functions
        result = str(eval(expr, {"__builtins__": None}, math.__dict__))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Scientific Calculator")
    root.geometry("350x400")

    display = StringVar()
    entry = Entry(root, textvariable=display, font=('Arial', 18))
    entry.grid(columnspan=6, ipadx=100, ipady=10)

    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('(', 2, 4), (')', 2, 5),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('^', 3, 4), ('sqrt(', 3, 5),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('log(', 4, 4), ('ln(', 4, 5),
        ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('sin(', 5, 4), ('cos(', 5, 5),
        ('Clear', 6, 0), ('tan(', 6, 1), ('pi', 6, 2), ('e', 6, 3), ('abs(', 6, 4), ('exp(', 6, 5)
    ]

    for (text, row, col) in buttons:
        action = lambda x=text: press(x) if x not in ['=', 'Clear'] else equal() if x == '=' else clear()
        Button(root, text=text, command=action, height=2, width=7, bg='red').grid(row=row, column=col, padx=1, pady=1)

    root.mainloop()
