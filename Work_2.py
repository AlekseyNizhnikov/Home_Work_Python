# Задание 1: Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.


# def sumNumbers(number):
#     list_number = number.split(",")
#     if(len(list_number) < 2):
#         list_number = number.split(".")

#     result = 0
#     for i in range(2):
#         for j in range(len(list_number[i])):
#             result += int(list_number[i][j])

#     print(f"Сумма цифр числа: {result}")

# number = input("Введите вещественное число: ")
# sumNumbers(number)


# Задание 2: Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.


# def multiNumbers(number):
    # result = 1
    # list_numbers = []

    # for i in range(1, number + 1):
    #         result *= i
    #         list_numbers.append(result)

    # print(f"Набор произведений: {list_numbers}")


# number = int(input("Введите число: "))
# multiNumbers(number)

# Задача 3: Задайте список из n чисел последовательности (1 + 1/n)^n и выведите
# на экран их сумму.


# def sumNumbers(number):
#     dict_result = {}

#     for i in range(1, number + 1):
#         dict_result[i] = round((1 + 1 / i) ** i, 2)

#     print(f"Сумма последовательности: {dict_result}")


# number = int(input("Введите число: "))
# sumNumbers(number)

# Задача 4:Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.

# import random


# def genNumber(number):
#     list_numbers = []

#     for _ in range(-number, number):
#         list_numbers.append(random.randint(0, 10))

#     print(f"Полученный список: {list_numbers}")
#     return list_numbers


# def multiNumbers(number):
#     list_numb = genNumber(number)
    
#     numb_A = int(input("Введите позицию первого множителя: "))
#     numb_B = int(input("Введите позицию второго множителя: "))

#     result = list_numb[numb_A] * list_numb[numb_B]

#     print(f"Результат произведения: {result}")


# number = int(input("Укажите длину списка: "))
# multiNumbers(number)

# Задача 5: Реализуйте алгоритм перемешивания списка.
# import random


# def mixList(input_list):
#     result = input_list

#     for i in range(len(input_list)):
#         index_list = random.randint(0, len(input_list) - 1)

#         result[index_list], result[i] = result[i], result[index_list]

#     print(f"Результат работы: {result}")


# list_numbers = [1, 2 ,3 ,4, 5, 6, 7, 8, 9]
# print(f"Исходный список:  {list_numbers}")

# mixList(list_numbers)