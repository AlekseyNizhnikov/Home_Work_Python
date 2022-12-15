from app.controller.controller import init_cntr

"""Цикл выбора интерфейса."""
while True:
    print("Выберите один из вариантов:\n1 -> Управление через графический интерфейс.\n2 -> Управление через телеграм-бота.")
    interface = input("-> ")
    if (interface == "1" or interface == "2"): break
    else: print("Попробуйте еще....")

init_cntr(interface)