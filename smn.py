from botcmds import howareu, hello, time, summe, helpme
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

updater.dispatcher.add_handler(CommandHandler('howareu', howareu))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', helpme))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('summe', summe))

print('server start')

updater.start_polling()
updater.idle()