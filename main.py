from dotenv import load_dotenv, dotenv_values

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
ENV = dotenv_values()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(ENV['TOKEN']).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()