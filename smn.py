from botcmds import *
from telegram.ext import Updater, CommandHandler


updater = Updater('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')
bot = telebot.TeleBot('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

updater.dispatcher.add_handler(CommandHandler('howareu', howareu))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', helpme))
updater.dispatcher.add_handler(CommandHandler('time', mytime))
# updater.dispatcher.add_handler(CommandHandler('nbook', nbook))
updater.dispatcher.add_handler(CommandHandler('nlist', nlist))
updater.dispatcher.add_handler(CommandHandler('nline', nline))
updater.dispatcher.add_handler(CommandHandler('nload', nload))
updater.dispatcher.add_handler(CommandHandler('ndel', ndel))
updater.dispatcher.add_handler(CommandHandler('nread', readnote))
updater.dispatcher.add_handler(CommandHandler('nimport', importnote))
updater.dispatcher.add_handler(CommandHandler('nexport', exportnote))
updater.dispatcher.add_handler(CommandHandler('math', math))

@bot.message_handler(command="/hi")
def hi(message):
    bot.send_message(message.chat_id, "Hello")

print('server start')

updater.start_polling()
updater.idle()