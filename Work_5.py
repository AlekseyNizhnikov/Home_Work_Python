# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def deletText(str_word, symbol):
#     result = (" ").join(filter(lambda word: symbol not in word, str_word.split()))
#     print(result)

# deletText("абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв", "абв")

# Задача 2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint


# def gameSweets():
#     sweets = 100
#     MAX_SWEETS = 28

#     bot = "N"
#     bot = input("Играть с ботом? (Y/N) ").upper()
#     gamers = randomStartGamer(bot)

#     while (sweets > 0):
#         for gamer in gamers:
#             sweets, gamer = funOne(gamer, sweets, MAX_SWEETS)
#             if (sweets == 0): break
        
#     print(f"Победил {gamer}") 


# def funOne(gamer, sweets, MAX_SWEETS):
#     while True:
#         if(gamer == "Компьютер"):
#             result = randint(1, 29)
#             if (sweets - result >= 0):
#                 print(f"{gamer} взял: {result} конфет.") 
#                 sweets -= result
#                 break
#         else:
#             result = int(input(f"Конфеты берет {gamer}: "))
#             if(result <= MAX_SWEETS) and (result <= sweets): 
#                 sweets -= result
#                 break

#     print(f"Конфет осталось: {sweets}\n")

#     return sweets, gamer


# def randomStartGamer(bot):
#     if(bot == "N"): 
#         gamers = ["Игрок 1", "Игрок 2"]
#         return gamers

#     elif(bot == "Y"): gamers = ["Игрок 1", "Компьютер"]
#     square = randint(0, 2)
#     if (square != 0): gamers[0], gamers[1] = gamers[1], gamers[0]
#     return gamers


# gameSweets()

# Задача 3: Создайте программу для игры в ""Крестики-нолики"".

# from tkinter import Tk, Button, PhotoImage, Label, Event
# from random import randint
# import copy


# # Главное окно программы.
# def mainWindow():
#     windows = Tk()
#     windows.title("Крестики-Нолики")
#     windows.geometry("300x365")
#     windows.resizable(0, 0)

#     count = 0
    

#     # Функция проверяет, есть ли победные комбинации.
#     def filterResult(list_i, name):
#         result = []

#         # Победные комбинации.
#         filter_X = ("XXX******", "***XXX***", "******XXX", "X***X***X", "X**X**X**", "*X**X**X*", "**X**X**X", "**X*X*X**")
#         filter_O = ("OOO******", "***OOO***", "******OOO", "O***O***O", "O**O**O**", "*O**O**O*", "**O**O**O", "**O*O*O**")

#         # Сверяем фильтр с текущим состоянием игрового поля
#         for filters in (filter_X, filter_O):
#             for i in range(len(filters)):
#                 result = copy.copy(list_i)

#                 for j in range(len(filter_X[i])):
#                     if (filter_X[i][j] == "*" and (result[j] == "X" or result[j] == "O")):
#                         result[j] = "*"
#                         continue
                    
#                     elif ((filter_X[i][j] == "X" or filter_X[i][j] == "O") and result[j] == "*"): break
                
#                 if("".join(result) == filters[i]):
#                     label_window["text"] = "ПОБЕДИЛ {}!".format(name)

#                     for i in range(len(result)):
#                         if (result[i] == "X" and name == "ИГРОК"):
#                             images_X_G = PhotoImage(file='1-1-1.gif')
#                             list_button[i].configure(image=images_X_G)
#                             list_button[i].image = images_X_G

#                         elif (result[i] == "O" and name == "SKYNET"):
#                             images_O_G = PhotoImage(file='2-2-2.gif')
#                             list_button[i].configure(image=images_O_G)
#                             list_button[i].image = images_O_G
                    
#                         else: 
#                             list_button[i]["state"] = "disabled"
#                             start_buttom["state"] = "normal"
#                     return True
#                 result = []

#         if (list_i.count("*") < 1 or list_i.count("X") > 4 or list_i.count("O") > 4): 
#             label_window["text"] = "НИЧЬЯ!"
#             start_buttom["state"] = "normal"
#             return True


#     # Функция описывающая работу человека (игрока).
#     def human(i):
#         name = "ИГРОК"
#         global list_i
#         list_i[i] = "X"
        
#         # Вставляем крестик в выбранное место.
#         images_X = PhotoImage(file='1-1.gif')
#         list_button[i].configure(image=images_X)
#         list_button[i].image = images_X

#         # Деактивируем выбранную кнопку.
#         list_button[i]["state"] = "disabled"
        
#         # Если НЕ появилась победная комбинация, даем сделать ход компьютеру.
#         if(not filterResult(list_i, name)):
#             computer(list_i)
#         else:
#             list_i = ["*", "*", "*", "*", "*", "*", "*", "*", "*"] 
#             return list_i


#     # Функция описывающая логику работы компьютера.
#     def computer(list_i):
#         name = "SKYNET"
#         dice = 0
        
#         # Зацикливаем выбор до тех пор пока не найдется свободное место для хода компьютера.
#         while True:
#             dice = randint(0, 8)

#             if (list_i[dice] == "*"): 
#                 list_i[dice] = "O" 
#                 break

#         # Выставляем кружочек в выбранное место.
#         images_O = PhotoImage(file='2-2.gif')
#         list_button[dice].configure(image=images_O)
#         list_button[dice].image = images_O

#         # Деактивируем выбранную кнопку.
#         list_button[dice]["state"] = "disabled"

#         # Если НЕ появилась победная комбинация, даем сделать ход человеку.
#         if(not filterResult(list_i, name)):
#             return list_i
#         else: return


#     # Функция рандомно выбирает ведущего игрока.
#     def startGame():
#         global list_i
#         list_i = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]

#         for i in range(len(list_button)):
#             list_button[i]["image"] = ""

#         flag = randint(0, 1)

#         # После старта игры, делаем кнопки игрового поля активными.
#         for i in range(len(list_button)):
#             list_button[i]["state"] = "normal"

#         # Если флаг = 1, то первым ходит компьютер.
#         if (flag == 1): computer(list_i)
        
#         start_buttom["state"] = "disabled"
#         return list_i


#     # Создаем 9 кнопок-ячеек.
#     list_button = [Button(windows, text="    ", font=("Time New Roman", 26), state="disabled", command=lambda x=i: human(x)) for i in range(9)] # for i in range(9): list_button[i].bind('<Button-1>', lambda x ,y = i: clicked(x, y))

#     # Размещаем кнопки в окне программы.
#     for i in range(3):
#             for j in range(3):
#                 list_button[count].grid(column=j, row=i, ipadx=15, ipady=15)
#                 count += 1

#     # Создаем кнопку старта игры и размещаем ее в окне программы.
#     start_buttom = Button(windows, text="НАЧАТЬ!", font=("Time New Roman", 12), command=startGame)
#     start_buttom.grid(column=0, row=3, columnspan=3, ipadx=109, ipady=3)

#     # Информирующее табло. Создаем и размещаем.
#     label_window = Label(windows, text="ПОЕХАЛИ!!!", font=("Time New Roman", 8))
#     label_window.grid(column=0, row=4, columnspan=3, ipadx=75, ipady=2)

#     windows.mainloop()


# mainWindow()

# Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def zipFun(file_name, result_file_name):
#     count = 1
#     keys, values = readData(file_name)

#     # Заносим значения в файл. Сжимаем данные дополнительно.
#     with open(result_file_name, "w", encoding="UTF-8") as res_file:
#         for i in range(len(keys)):
#             if (values[i] > 128):
#                 numb = values[i] // 128
#                 for _ in range(numb):
#                     res_file.write(keys[i] + str(128))
#                 res_file.write(keys[i] + str(values[i] - (128 * numb)))

#             elif (values[i] == 1):
#                 if (values[i + 1] == 1):
#                     res_file.write(keys[i])
#                     count += 1
#                 else:
#                     if(count != 1): res_file.write(keys[i] + f"-{str(count)}")
#                     else: res_file.write(keys[i] + str(count))
#                     count = 1

#             else: res_file.write(keys[i] + str(values[i]))


# # Четение данных из файла.
# def readData(file_name):
#         keys = []
#         values = []
#         list_elements = []
#         count = 1

#         # Записываем содержимое файла в список - побуквенно.
#         with open(file_name, "r", encoding="UTF-8") as file:
#             list_elements = tuple(file.read())

#         # Подсчитываем количество букв. и генерируем два списка с ключом и значением.
#         for i in range(len(list_elements) - 1):
#             if(list_elements[i] == list_elements[i + 1]): 
#                 count += 1
#                 if (i == len(list_elements) - 2):
#                     keys.append(list_elements[i + 1])
#                     values.append(count)
#                     count = 1
#             else:
#                 keys.append(list_elements[i])
#                 values.append(count)
#                 count = 1

#         return keys, values


# # Восстановление данных из файла.
# def recoveryData(file_name):

#     # Читаем данные файла
#     with open(file_name, "r", encoding="UTF-8") as file:
#         list_data = file.read()
    
#     # Восстанавливаем и записываем данные в файл.
#     with open("result_1.txt", "w", encoding="UTF-8") as res_file:
#         for i in range(len(list_data)):
#             if (list_data[i].isalpha()):
#                 if (list_data[i + 1].isdigit()):
#                     value = checkNumber(list_data[i + 1:i + 4])
#                     res_file.write(list_data[i] * int(value))
#                 else: res_file.write(list_data[i])
#             else: continue


# # Функция которая подсчитывает число повторений.
# def checkNumber(list_ii):
#     value = ""
#     for i in range(len(list_ii)): 
#         if (list_ii[i].isdigit()): value += list_ii[i]
#         else: return value
#     return value


# zipFun("example.txt", "result.txt")
# recoveryData("result.txt")