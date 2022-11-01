from telepot import *
from telegram.ext import CallbackContext
phonebook = ''

def pb (update: phonebook, context: CallbackContext):
    phonebook = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        phonebook += i