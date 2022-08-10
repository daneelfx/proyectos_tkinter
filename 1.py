import tkinter as tk
from tkinter import ttk

def greet():
  print(f'Hello, {user_name.get()}')

root = tk.Tk()
root.title('Greeter')

input_frame = ttk.Frame(root)
input_frame.pack(side = 'top', fill = 'x')

buttons_frame = ttk.Frame(root)
buttons_frame.pack(side = 'top', fill = 'x')



user_name = tk.StringVar()

name_label = ttk.Label(input_frame, text = 'Write your name')
name_label.pack(side = 'left')

name_entry = ttk.Entry(input_frame, width = 20, textvariable = user_name)
name_entry.pack(side = 'top', fill = 'x')
name_entry.focus()

greet_button = ttk.Button(buttons_frame, text = 'Greet', command = greet)
greet_button.pack(side = 'left', fill = 'x', expand = True)

quit_button = ttk.Button(buttons_frame, text = 'Quit', command = root.destroy)
quit_button.pack(side = 'left', fill = 'x', expand = True)

root.mainloop()