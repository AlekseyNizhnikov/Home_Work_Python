from telegram.ext import ApplicationBuilder, MessageHandler, filters
from app.view.bot_command import calculate

from app.view.config_bot import token_bot # Подтягиваем токен бота.

"""Запускаем телеграм-бота."""
def init_bot():
    token = token_bot()

    if not token: print("Добавьте в файл token.txt - token!!!".upper())
    else:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
        app.run_polling()

    
