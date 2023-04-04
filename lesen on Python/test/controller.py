import view
import model_menu
from tkinter import *
from tkinter import ttk 

frm = None


def button_count_days_click():
    global frm
    x = model_menu.count_days()
    label_answer = ttk.Label(frm, text=f'{x}')
    label_answer.grid(row=2, column=0)

def button_calculate_click():
    global frm
    x = model_menu.calculate_number()
    label_answer = ttk.Label(frm, text=f'{x}')
    label_answer.grid(row=2, column=1)

def button_random_click():
    global frm
    x = model_menu.create_random_number()
    label_answer = ttk.Label(frm, text=f'{x}')
    label_answer.grid(row=2, column=2)

def start():
    global frm
    # view.create_menu()
    # select()
    root = Tk()
    frm = ttk.Frame(root, padding=30)
    frm.grid()

    label_calculate = ttk.Label(frm, text='Калькулятор')
    label_calculate.grid(row=0, column=1)

    button_count_days = ttk.Button(frm, text='Cколько дней до 8 марта?', command=button_count_days_click)
    button_count_days.grid(row=1, column=0)

    button_calculate = ttk.Button(frm, text='Вычислить 2+2?', command=button_calculate_click)
    button_calculate.grid(row=1, column=1)
    
    button_random = ttk.Button(frm, text='Сгенерировать случайное число', command=button_random_click)
    button_random.grid(row=1, column=2)

    button_exit = ttk.Button(frm, text='Выход', command=button_random_click)
    button_exit.grid(row=3, column=1)

    root.mainloop()

def select():
    view.input_number()
    number = int(input())
    model_menu.select(number)

