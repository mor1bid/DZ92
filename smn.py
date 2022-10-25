# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def howareu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE').build()

# app.add_handler(CommandHandler("howareu", howareu))

# app.run_polling()

from botcmds import howareu, hello, summe
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

updater.dispatcher.add_handler(CommandHandler('howareu', howareu))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('summe', summe))
print('server start')
updater.start_polling()
updater.idle()