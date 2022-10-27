from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def mnm1(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    msg.pop(0)
    with open('Phonebook.txt', 'a') as file:
        for i in msg:
            file.write(' \n')
            file.write(i)
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread')