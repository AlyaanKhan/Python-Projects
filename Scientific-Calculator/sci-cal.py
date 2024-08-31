import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

color1 = "#FFD700"
color2 = "#FFFFE0"
button_bg_color = color1
button_fg_color = "#000000"
display_bg_color = color2
display_fg_color = "#000000"

display = tk.Entry(root, font=('Helvetica', 20), bg=display_bg_color, fg=display_fg_color, borderwidth=10, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def click_button(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(item))

def clear_display():
    display.delete(0, tk.END)

def evaluate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def scientific_function(func):
    try:
        value = display.get()
        if func == "sin":
            result = str(math.sin(math.radians(float(value))))
        elif func == "cos":
            result = str(math.cos(math.radians(float(value))))
        elif func == "tan":
            result = str(math.tan(math.radians(float(value))))
        elif func == "log":
            result = str(math.log10(float(value)))
        elif func == "sqrt":
            result = str(math.sqrt(float(value)))
        elif func == "pow":
            result = str(math.pow(float(value), 2))
        
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

scientific_buttons = [
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
    ('sqrt', 6, 0), ('pow', 6, 1), ('C', 6, 2)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Helvetica', 15), bg=button_bg_color, fg=button_fg_color, borderwidth=5, relief=tk.RAISED, command=evaluate)
    else:
        button = tk.Button(root, text=text, font=('Helvetica', 15), bg=button_bg_color, fg=button_fg_color, borderwidth=5, relief=tk.RAISED, command=lambda t=text: click_button(t))
    
    button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

for (text, row, col) in scientific_buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=('Helvetica', 15), bg="red", fg=button_fg_color, borderwidth=5, relief=tk.RAISED, command=clear_display)
    else:
        button = tk.Button(root, text=text, font=('Helvetica', 15), bg=button_bg_color, fg=button_fg_color, borderwidth=5, relief=tk.RAISED, command=lambda t=text: scientific_function(t))
    
    button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
