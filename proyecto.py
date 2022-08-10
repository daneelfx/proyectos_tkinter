import tkinter as tk
from tkinter import ttk
from tkinter import font
from turtle import bgcolor


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
ratio = screen_width / screen_height

root.geometry(f'{int(screen_height * 0.6 * ratio)}x{int(screen_height * 0.6)}')
root.title('Matriz / Monitoreo / Alcón')


options_frame_style = ttk.Style()
options_frame_style.configure('OPTIONS_FRAME.TButton')

options_frame = ttk.Frame(root, style = 'OPTIONS_FRAME.TButton')
options_frame.pack(side = 'bottom', fill = 'both')

monitoring_button_style = ttk.Style()
monitoring_button_style.configure('MONITORING.TButton', padding = 6, font = ('Calibri'))

matrix_button_button_style = ttk.Style()
matrix_button_button_style.configure('MATRIX.TButton', padding = 6, font = ('Calibri'))

alcon_button_style = ttk.Style()
alcon_button_style.configure('ALCON.TButton', padding = 6, font = ('Calibri'))

monitoring_button = ttk.Button(options_frame, text = 'MONITOREO', command = lambda: print('MONITOREO'), style = 'MONITORING.TButton')
monitoring_button.pack(side = 'left', expand = True)

matrix_button = ttk.Button(options_frame, text = 'MATRIZ', command = lambda: print('MATRIZ'), style = 'MATRIX.TButton')
matrix_button.pack(side = 'left', expand = True)

alcon_button = ttk.Button(options_frame, text = 'ALCÓN', command = lambda: print('ALCON'), style = 'ALCON.TButton')
alcon_button.pack(side = 'left', expand = True)


root.mainloop()