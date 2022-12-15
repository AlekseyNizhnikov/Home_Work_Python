from app.view.view import init_tk
from app.view.view_bot import init_bot
from app.controller.log import log, log_error

"""Функция обрабатывает нажатие клавиши Enter или "="."""
def handlerEnter(number, text, user_name="Admin"):
    if(str(number) == "Enter"):
        result = calculation(text, user_name)
        log(user_name, text, result)
        return result
    else:
        return number

"""Функция производит проверку корректности ввода и выполняет вычисление."""
def calculation(text, user_name):
    result = 0.0

    list_operate = ["+", "-", "*", "/"]
    for oper in list_operate:
        text = text.replace(oper, f" {oper} ")

    new_text = text.split()

    if(not new_text): return "0.0"

    elif(len(new_text) == 1):
        text_error = "Некорректный ввод!"
        log_error(user_name,  text, text_error)
        return "Некорректный ввод!"
        
    elif(new_text[0] == "-"):
        new_text[1] = float(new_text[1]) * (-1.0)
        new_text.pop(0)

    for i in range(len(new_text) - 1):
        try:
            match new_text[i]:
                case "+": result += float(new_text[i - 1]) + float(new_text[i + 1])
                case "-": result += float(new_text[i - 1]) - float(new_text[i + 1])
                case "*": result += float(new_text[i - 1]) * float(new_text[i + 1])
                case "/": 
                    try:
                        result += float(new_text[i - 1]) / float(new_text[i + 1])
                    except ZeroDivisionError:
                        text_error = "Деление на 0!"
                        log_error(user_name,  text, text_error)
                        return text_error
        except ValueError:
            text_error = "Некорректный ввод!"
            log_error(user_name,  text, text_error)
            return "Некорректный ввод"

    return round(result, 6)

"""Выбираем интерфейс работы программы и подтягиваем нужный."""
def init_cntr(interface):
    if( interface == "1"):
        init_tk() # Tkinter
    else:
        init_bot() # Telegram-bot