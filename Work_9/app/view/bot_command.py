from telegram import Update
from telegram.ext import ContextTypes

"""Обрабатываем входное сообщение. При возможности выполняем вычисления и возвращаем результат."""
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    user_name = update.effective_user.first_name
    result = handlerInput("Enter", msg, user_name)
    
    await update.message.reply_text(f'Результат: {result}')

"""Обмен данными с контроллером."""
def handlerInput(command, msg, user_name):
    from app.controller.controller import handlerEnter
    
    result = handlerEnter(command, msg, user_name)
    return result

