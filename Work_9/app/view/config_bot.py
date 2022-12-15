def token_bot():
    try:
        with open("app/view/token.txt", "r", encoding="UTF-8") as file:
            token = file.readline()
        return token
    except FileNotFoundError:
        with open("app/view/token.txt", "w", encoding="UTF-8"): pass
        print("Добавьте в файл token.txt - token!!!".upper())