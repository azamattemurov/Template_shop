from telegram.ext import CommandHandler, MessageHandler, filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salom! Men Telegram botman.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Botni ishga tushirish uchun
application.run_polling()
