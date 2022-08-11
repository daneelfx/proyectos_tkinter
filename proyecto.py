import tkinter as tk
from tkinter import ttk
from tkinter import font
from turtle import bgcolor, color, width

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

try:
  from ctypes import windll
  windll.shcore.SetProcessDpiAwareness(1)
except:
 pass

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
ratio = screen_width / screen_height

root.geometry(f'{int(screen_height * 0.6 * ratio)}x{int(screen_height * 0.6)}')
root.resizable(False, False)

root.title('Matriz / Monitoreo / Alcón')


def select_file():
    filetypes = (
        ('Excel files', '*.xlsx | *.xls'),
    )

    filename = fd.askopenfilename(
        title = 'Seleccione archivo Excel',
        initialdir ='*/',
        filetypes = filetypes)

    showinfo(
        title = 'Archivo seleccionado',
        message = filename
    )

# MONITOREO - INICIO

monitoring_frame_style = ttk.Style()
monitoring_frame_style.configure('MONITORING_FRAME.TFrame', background = '#E26D5C')

monitoring_frame = ttk.Frame(root, style = 'MONITORING_FRAME.TFrame')
monitoring_frame.pack(side = 'top', fill = 'both', expand = True)

monitoring_title_style = ttk.Style()
monitoring_title_style.configure('MONITORING_TITLE.TLabel', foreground = '#fff', background = '#E26D5C', font = ('Calibri', 35), padding = (0, 20))

monitoring_title = ttk.Label(monitoring_frame, text = 'SELECCIONE UN TIPO DE ARCHIVO', style = 'MONITORING_TITLE.TLabel')
monitoring_title.pack()

monitoring_inner_buttons_style = ttk.Style()
monitoring_inner_buttons_style.configure('MONITORING_INNER_BUTTONS.TButton', padding = (10, 6), font = ('Calibri'), width = 25)

base_negocio_button = ttk.Button(monitoring_frame, text = 'BASE NEGOCIOS', style = 'MONITORING_INNER_BUTTONS.TButton', command = select_file)
base_negocio_button.pack()

base_deterioro_button = ttk.Button(monitoring_frame, text = 'BASE DETERIORO', style = 'MONITORING_INNER_BUTTONS.TButton', command = select_file)
base_deterioro_button.pack()

base_provision_button = ttk.Button(monitoring_frame, text = 'BASE PROVISIÓN', style = 'MONITORING_INNER_BUTTONS.TButton', command = select_file)
base_provision_button.pack()

base_super_button = ttk.Button(monitoring_frame, text = 'BASE SUPER', style = 'MONITORING_INNER_BUTTONS.TButton', command = select_file)
base_super_button.pack()

# MONITOREO - FINAL

options_frame_style = ttk.Style()
options_frame_style.configure('OPTIONS_FRAME.TButton')

options_frame = ttk.Frame(root, style = 'OPTIONS_FRAME.TButton', padding = 30)
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