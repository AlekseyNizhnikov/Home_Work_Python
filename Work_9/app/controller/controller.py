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

"""Обработчик строки. Ищем операторы и выполняем необходимые действия. Возвращаем список или строку."""
def handlerOperate(new_text, operate):
    while True:
        if(new_text.count(operate) >= 1):
            i = new_text.index(operate)
            try:
                match operate:
                    case "-": 
                        new_text[i] = float(new_text[i + 1]) * -1.0
                        new_text.pop(i + 1)

                    case "*": 
                        new_text[i] = float(new_text[i - 1]) * float(new_text[i + 1])
                        new_text.pop(i - 1)
                        new_text.pop(i)

                    case "/":
                        try:
                            new_text[i] = float(new_text[i - 1]) / float(new_text[i + 1])
                            new_text.pop(i - 1)
                            new_text.pop(i)

                        except ZeroDivisionError:
                            return "Деление на 0!"

                    case "+":
                        new_text[i] = float(new_text[i - 1]) + float(new_text[i + 1])
                        new_text.pop(i - 1)
                        new_text.pop(i)

            except ValueError:
                return "Некорректный ввод!"
            
        else: break
    return new_text

"""Функция производит проверку корректности ввода и выполняет вычисление."""
def calculation(text, user_name):

    list_operate = ["*", "/", "+", "-"]
    for oper in list_operate:
        text = text.replace(oper, f" {oper} ")
    new_text = text.split()

    if(not new_text): return "0.0"

    elif(len(new_text) == 1):
        text_error = "Некорректный ввод!"
        log_error(user_name,  text, text_error)
        return "Некорректный ввод!"

    new_text = handlerOperate(new_text, "-")
    new_text = handlerOperate(new_text, "*")
    new_text = handlerOperate(new_text, "/")
    new_text = handlerOperate(new_text, "+")


    if(len(new_text) > 1):
        new_text[0] = sum(new_text)

    try:
        return round(new_text[0], 6)
    except TypeError:
        log(user_name, text, new_text)
        return new_text

"""Выбираем интерфейс работы программы и подтягиваем нужный."""
def init_cntr(interface):
    if( interface == "1"):
        init_tk() # Tkinter
    else:
        init_bot() # Telegram-bot