from tkinter import *
from app.view.config_tk import config_tk

result = ""

"""Создаем кнопки и размещаем их на рабочем окне программы."""
def creatButton(windows, font_text, win_entry):
    numb_button = [Button(windows, text=i, font=font_text, command=lambda event=Event, x=i, y=win_entry: handlerCommand(event, x, y), width=5, height=1) for i in range(1, 10)]

    count = 0
    for i in range(2, 5):
        for j in range(3):
            if (j == 0): numb_button[count].grid(row=i, column=j, padx=3, pady=0)
            else: numb_button[count].grid(row=i, column=j, padx=0, pady=0)
            count += 1

    zero_button = Button(windows, text="0", font=font_text, command=lambda event=Event, x="0", y=win_entry: handlerCommand(event, x, y), width=11, height=1)
    zero_button.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

    enter_button = Button(windows, text="=", font=("Time New Roman", 10), command=lambda event=Event, x="Enter", y=win_entry: handlerCommand(event, x, y), width=7, height=1)
    enter_button.grid(row=0, column=3, padx=0, pady=0)

    point_button = Button(windows, text=".", font=font_text, command=lambda event=Event, x=".", y=win_entry: handlerCommand(event, x, y), width=5, height=1)
    point_button.grid(row=5, column=2, padx=0, pady=0)

    operates = [" / "," * ", " - ", " + "]
    operat_button = [Button(windows, text=operate, font=font_text, command=lambda event=Event, x=operate, y=win_entry: handlerCommand(event, x, y), width=5, height=1) for operate in operates]

    for i in range(4):
        operat_button[i].grid(row=i+2, column=3, padx=3, pady=0)

    clear_button = Button(windows, text="C", font=font_text, command=lambda event=Event, x="C", y=win_entry: handlerCommand(event, x, y), width=5, height=1)
    clear_button.grid(row=1, column=3, padx=3, pady=0)

"""Функция передает полученное значение в контроллер."""
def handlerCommand(event, command, out):
    from app.controller.controller import handlerEnter
    
    global result
    result += str(command)
    result_text = handlerEnter(command, out.get())

    out.delete(0, END) 

    if (command == "Enter"):
        out.insert(END, f" {result_text} ")
        result = ""

    elif (command == "C"): result = ""

    else: out.insert(END, f"{result} ")

"""Функция создает окно ввода/вывода."""
def creatWinEntry(windows):
    win_entry = Entry(windows, width=17, font=("Time New Roman", 16), justify=RIGHT)
    win_entry.grid(row=0, column=0, columnspan=3, padx=3, pady=3)
    win_entry.focus_set()
    win_entry.bind("<Return>", lambda event=Event, x="Enter", y=win_entry: handlerCommand(event, x, y))

    return win_entry

"""Функция подтягивает все графические элементы окна программы."""
def controllerGUI(windows, font_text):
    win_entry = creatWinEntry(windows)
    creatButton(windows, font_text, win_entry)

"""Инициализация настроек и создание рабочего окна программы."""
def init_tk():
    windows = Tk()
    
    font_text = config_tk(windows)
    controllerGUI(windows, font_text)

    windows.mainloop()