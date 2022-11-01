from random import randint, random

# Задача 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

# def sumNumbers(numbers):
#     list_numbers = randNumbers(numbers)
#     result = 0

#     for i in range(0, len(list_numbers), 2):
#         result += list_numbers[i]

#     print(f"Сумма элементов: {result}")


# def randNumbers(number):
#     numbers = []

#     for _ in range(number):
#         numbers.append(randint(0, 10))

#     print(f"Список случайных чисел:\n{numbers}")
#     return numbers


# number = int(input("Введите длину списка: "))
# sumNumbers(number)

# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def multiNumbers(numbers):
#     list_numbers = randNumbers(numbers)
#     result = []

#     for i in range(int(numbers * .5 + .5)):
#         result.append(list_numbers[i] * list_numbers[(number - 1) - i])

#     print(f"Список произведения пар чисел:\n{result}")


# def randNumbers(number):
#     numbers = []

#     for _ in range(number):
#         numbers.append(randint(0, 10))

#     print(f"Список случайных чисел:\n{numbers}")
#     return numbers


# number = int(input("Введите длину списка: "))
# multiNumbers(number)


# Задача 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# def difNumber(numbers):
#     list_numbers = randNumbers(numbers)

#     max_value = min_value = round(list_numbers[0] % 1, 2)
#     result = value = 0

#     for numb in list_numbers:
#         value = round(numb % 1, 2)

#         if(value < min_value): min_value = value
#         elif(value > max_value): max_value = value

#     result = round(max_value - min_value, 2)
#     print(f"Разница между max и min: {result}")


# def randNumbers(number):
#     numbers = []

#     for _ in range(number):
#         numbers.append(round(random() * 10, 2))

#     print(f"Список случайных чисел:\n{numbers}")
#     return numbers


# number = int(input("Введите длину списка: "))
# difNumber(number)


# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def binNumber(dec_number):
#     number = dec_number
#     result = ""

#     while (number > 0):
#         if(number % 2 == 0): result = "0" + result
#         else: result = "1" + result

#         number = int(number / 2)

#     print(f"Двоичное представление числа {dec_number}: {result}")


# number = int(input("Введите десятичное число: "))
# binNumber(number)


# Задание 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def funFibonache(number):
    list_fib = [-1, 0, 1]
    result = None

    for i in range(1, number):
        result = list_fib[i + i] + list_fib[(i + i) - 1]
        list_fib.append(result)
        list_fib.insert(0, result * (-1))

    print(f"Негафибоначчи: {list_fib}")


number = int(input("Введите число: "))
funFibonache(number)