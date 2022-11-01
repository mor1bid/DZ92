from telepot import *
from telegram import Update
from telegram.ext import CallbackContext
from spiek import *
phonebook = ''

def nbook (update: Update, context: CallbackContext):
    log(update, context)
    phonebook = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        phonebook += i
    update.message.reply_text('Done.')
    return phonebook