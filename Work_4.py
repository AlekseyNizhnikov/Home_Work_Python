# Задача 1: Вычислить число Пи c заданной точностью d

# def calc_Pi(precision):
#     number_Pi = 0.0
#     result = ""
#     count = 0

#     while(precision // 1 <= 0):
#         count += 1
#         precision *= 10

#     for i in range(1, 1_000_000, 2):
#         number_Pi += 1 / i
#         number_Pi *= -1

#     result = str(number_Pi * 4)
#     print(f"Число Пи с заданной точностью: {result[:2 + count]}")


# precision = float(input("Укажите точность: "))
# calc_Pi(precision)

# Задача 2: Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

# def natureNumber(number):
#     list_number = []
#     flag = True

#     for i in range(2, number):
#         for j in range(2, number):
#             if (j != i):
#                 if (i % j == 0): 
#                     flag = False
#                     break
#                 else: 
#                     flag = True
#                     continue
#         if (flag == True):
#             list_number.append(i)

#     result = list(filter(lambda x: not number % x, list_number))
#     print(result)

# number = int(input("Введите натуральное число: "))
# natureNumber(number)


# Задача 3: Задайте последовательность цифр. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# def copyNumbers(str_numbers):
#     list_number = list(str_numbers)
#     result = filter(lambda i: list_number.count(i) < 2, list_number)

#     print(f"Неповторяющиеся цифры: {list(result)}")


# numbers = input("Введите последовательность чисел: ")
# copyNumbers(numbers)


# Задача 4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
#  многочлена и записать в файл многочлен степени k.
#  k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля.
#  Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени.
#  Записываем результат в файл.

# from random import randint

# # Функция генерирует полином level-степени.
# def creatPolynomial(level):
#     coefficient = 0

#     with open("example_2.txt", "w", encoding="UTF-8") as ex:
#         for i in range(level, -1, -1):
#             coefficient = randint(-100, 100)
#             superscript = formatSuperscript(i)

#             if(i == level):
#                 ex.write(f"{coefficient}x" + superscript)
#                 continue
#             if(i == 0):
#                 if(coefficient > 0): ex.write(f" + {coefficient}")
#                 elif(coefficient < 0): ex.write(f" - {coefficient * (-1)}")
#             else:
#                 if(coefficient == 0): continue
#                 elif(coefficient > 0): 
#                     if(i == 1): ex.write(f" + {coefficient}x")
#                     else: ex.write(f" + {coefficient}x" + superscript)
#                 elif(coefficient < 0): 
#                     if(i == 1): ex.write(f" - {coefficient * (-1)}x")
#                     else: ex.write(f" - {coefficient * (-1)}x" + superscript)

#         ex.write(" = 0")


# # Функция форматирования степени в верхний индекс.
# def formatSuperscript(level):
#     dict_unicode = {0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074", 5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}
#     superscript = ""

#     for i in str(level):
#         for j, k in dict_unicode.items():
#             if (i == k): superscript += str(j)
#             if (i == str(j)):
#                 superscript += str(k)

#     return superscript


# level = int(input("Введите максимальную степень полинома: "))
# creatPolynomial(level)

# Задача 5: Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# Функция считывает содержимое двух файлов и выполняет сложение полиномов.
# def sumPolynomial(*args):
#     file = [*args]
#     polynomial = []
#     dict_coefficient = dict()

#     for i in range(len(file)):
#         with open(file[i], "r", encoding="UTF-8-sig") as fp:
#             polynomial.append(fp.read())

#         polynomial[i] = polynomial[i].replace(" + ", " ")
#         polynomial[i] = polynomial[i].replace(" - ", " -")
#         polynomial[i] = polynomial[i].split(" ")

#         for j in range(len(polynomial[i]) - 2):
#             polynomial[i][j] = polynomial[i][j].split("x")
            
#             if(polynomial[i][j][0] == ''): polynomial[i][j][0] = "1"
            
#             elif(len(polynomial[i][j]) == 1): polynomial[i][j].append("⁰")
#             elif(polynomial[i][j][1] == ''): polynomial[i][j][1] = "¹"

#             superscript = int(formatSuperscript(polynomial[i][j][1]))
#             if (not superscript in dict_coefficient):
#                 dict_coefficient[superscript] = int(polynomial[i][j][0])
#             else:
#                 dict_coefficient[superscript] = dict_coefficient[superscript] + int(polynomial[i][j][0])

#     keys = sorted(dict_coefficient, reverse=True)
#     writePolynomial(keys, dict_coefficient)
    

# # Форматированная запись полинома.
# def writePolynomial(keys, dict_coefficient):
#     result = ""

#     for i in range(len(keys)): 
#         if (i == 0): result += f"{dict_coefficient[keys[i]]}x{formatSuperscript(keys[i])} "
#         else: 
#             if (dict_coefficient[keys[i]] > 0): 
#                 if (keys[i] == 1): result += f"+ {dict_coefficient[keys[i]]}x "
#                 elif (keys[i] == 0): result += f"+ {dict_coefficient[keys[i]]} "
#                 else: result += f"+ {dict_coefficient[keys[i]]}x{formatSuperscript(keys[i])} "
#             elif (dict_coefficient[keys[i]] < 0): 
#                 if (keys[i] == 1): result += f"- {dict_coefficient[keys[i]] * -1}x "
#                 elif (keys[i] == 0): result += f"- {dict_coefficient[keys[i]] * -1} "
#                 else: result += f"- {int(dict_coefficient[keys[i]]) * -1}x{formatSuperscript(keys[i])} "

#     with open("result.txt", "w", encoding="UTF-8-sig") as res:
#         res.write(result + " = 0")


# # Функция форматирования степени в верхний индекс.
# def formatSuperscript(level):
#     dict_unicode = {0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074", 5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}
#     superscript = ""

#     for i in str(level):
#         for j, k in dict_unicode.items():
#             if (i == k): superscript += str(j)
#             if (i == str(j)):
#                 superscript += str(k)

#     return superscript


# sumPolynomial("example_1.txt", "example_2.txt")