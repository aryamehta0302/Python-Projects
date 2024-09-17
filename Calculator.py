import tkinter as tk
from tkinter import StringVar
from tkinter.messagebox import showerror

def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')


def submit(strvar: StringVar):
    operation = strvar.get()
    try:
        strvar.set(f"{operation}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a valid equation!')


def handle_keypress(event, strvar: StringVar):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '(', ')', '.']:
        add_text(key, strvar)
    elif key == '\r':  
        submit(strvar)
    elif key == '\x08':  
        strvar.set(strvar.get()[:-1])


root = tk.Tk()
root.title("Modern Calculator")
root.geometry('360x550')
root.resizable(0, 0)  
root.configure(background='#1C1C1C')


entry_strvar = StringVar(root)


button_bg = '#4CAF50'          
button_hover_bg = '#66BB6A'   
button_text_color = '#FFFFFF'  
entry_bg = '#333333'          
entry_text_color = '#FFFFFF'   


eqn_entry = tk.Entry(root, justify=tk.RIGHT, textvariable=entry_strvar, font=("Arial", 24), fg=entry_text_color, bg=entry_bg, bd=10, relief=tk.FLAT)
eqn_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")


def on_enter(e):
    e.widget['background'] = button_hover_bg

def on_leave(e):
    e.widget['background'] = button_bg


def create_button(root, text, row, col, command):
    btn = tk.Button(root, text=text, font=("Arial", 14), bg=button_bg, fg=button_text_color, height=2, width=5, relief=tk.FLAT, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

button_config = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3),
]

for (text, row, col) in button_config:
    create_button(root, text, row, col, lambda t=text: add_text(t, entry_strvar))


create_button(root, '=', 5, 2, lambda: submit(entry_strvar))
create_button(root, '/', 5, 3, lambda: add_text('/', entry_strvar))
create_button(root, 'C', 5, 0, lambda: entry_strvar.set(entry_strvar.get()[:-1]))
create_button(root, 'AC', 5, 1, lambda: entry_strvar.set(''))

root.bind('<Key>', lambda event: handle_keypress(event, entry_strvar))


exit_btn = tk.Button(root, text='OK', font=("Arial", 14), bg='#F44336', fg='white', height=2, width=22, relief=tk.FLAT, command=lambda: root.destroy())
exit_btn.grid(row=6, column=0, columnspan=4, pady=10)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

