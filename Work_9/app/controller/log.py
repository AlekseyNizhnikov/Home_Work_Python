from datetime import datetime

"""Записываем данные в файл, все что вводил пользователь, его имя и дату."""
def log(user_name, exercise, result):
    with open("log.txt", "a", encoding="UTF-8") as file:
        file.write(f"{datetime.now().strftime('%m/%d/%y %H:%M:%S')} Пользователь: {user_name} Запрос: {exercise.ljust(20)} Ответ: {result}\n")

"""Записываем данные в файл, если поймали ошибку. Деление на 0 или некорректный ввод."""
def log_error(user_name, exercise, result):
    with open("log.txt", "a", encoding="UTF-8") as file:
        file.write(f"   {datetime.now().strftime('%m/%d/%y %H:%M:%S')} Пользователь: {user_name} Запрос: {exercise.ljust(20)} Ответ: {result}\n")