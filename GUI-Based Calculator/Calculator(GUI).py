import tkinter as tk

def button_click(event):
    current = display_var.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif text == "C":
        display_var.set("")
    else:
        display_var.set(current + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

root.configure(bg="#333333")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), justify="right", bd=5, relief="ridge", bg="#444444", fg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 18), padx=20, pady=10, bd=2, relief="ridge", bg="#555555", fg="white")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
