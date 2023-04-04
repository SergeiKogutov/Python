from tkinter import *  
from tkinter import ttk
from tkinter import scrolledtext   
    
  
# def clicked():  
#     res = "Привет {}".format(txt.get())  
#     lbl.configure(text=res)  
  
  
# window = Tk()  
# window.title("Добро пожаловать в приложение PythonRu")  
# window.geometry('400x250')  
# lbl = Label(window, text="Привет")  
# lbl.grid(column=0, row=0)  
# txt = Entry(window,width=10)  
# txt.grid(column=1, row=0)  
# btn = Button(window, text="Клик!", command=clicked)  
# btn.grid(column=2, row=0)
# combo = ttk.Combobox(window)  
# combo['values'] = (1, 2, 3, 4, 5, "Текст")  
# combo.current(1)  # установите вариант по умолчанию  
# combo.grid(column=0, row=1) 
# chk_state = BooleanVar()  
# chk_state.set(0)  # задайте проверку состояния чекбокса  
# chk = Checkbutton(window, text='Выбрать', var=chk_state)  
# chk.grid(column=1, row=1)
# rad1 = Radiobutton(window, text='Первый', value=1)  
# rad2 = Radiobutton(window, text='Второй', value=2)  
# rad3 = Radiobutton(window, text='Третий', value=3)  
# rad1.grid(column=0, row=3)  
# rad2.grid(column=1, row=3)  
# rad3.grid(column=2, row=3)      
# window.mainloop()
def clicked():  
    lbl.configure(text=selected.get())  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
selected = IntVar()  
rad1 = Radiobutton(window,text='Первый', value=1, variable=selected)  
rad2 = Radiobutton(window,text='Второй', value=2, variable=selected)  
rad3 = Radiobutton(window,text='Третий', value=3, variable=selected)  
btn = Button(window, text="Клик", command=clicked)  
lbl = Label(window)  
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0)  
btn.grid(column=3, row=0)  
lbl.grid(column=0, row=1)
txt = scrolledtext.ScrolledText(window, width=40, height=10)  
txt.grid(column=0, row=3)  
window.mainloop()