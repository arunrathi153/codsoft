import tkinter as tk

def click(event):
    current = str(entry.get())
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
            entry.delete(0, tk.END)
    else:
            entry.insert(tk.END, button_text)

#window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

#Input Field
entry = tk.Entry(root, font="Arial 20",borderwidth=2, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15,padx=10, pady=10)

#Button Layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],    
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(fill="both", expand=True)
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18",height=2, width=5)
        btn.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        btn.bind("<Button-1>", click)

#start the application
root.mainloop()        