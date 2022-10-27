from botcmds import *
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

updater.dispatcher.add_handler(CommandHandler('howareu', howareu))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', helpme))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('summe', summe))
updater.dispatcher.add_handler(CommandHandler('nmake', makenote))
updater.dispatcher.add_handler(CommandHandler('nread', readnote))
updater.dispatcher.add_handler(CommandHandler('nimport', importnote))

print('server start')

updater.start_polling()
updater.idle()