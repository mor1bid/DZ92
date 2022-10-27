from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spiek import *

def howareu(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'How bout conquering the world, {update.effective_user.first_name}?')

def hello(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def summe(update: Update, context: CallbackContext):
    log(update, context)
    # update.message.reply_text(f'Enter 2 digits please:')
    msg = update.message.text
    digs = msg.split()
    numa = int(digs[1])
    numb = int(digs[2])
    update.message.reply_text(f'Here ye go: {numb} + {numa} = {numb+numa}')

def time(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Its {datetime.datetime.now().time()}')

def helpme(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Here ye go:\n/hi\n/howareu\n/time\n/summe\n/makenote\n/readnote\n')

def makenote (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.strip('/makenote')
    with open('DZPhonebook.txt', 'a') as file:
        file.write(msg)
        file.write('\n')
        update.message.reply_text('Done. For readin your notes, type /readnote')

def readnote (update: Update, context: CallbackContext):
    log(update, context)
    text = ''
    msg = update.message.text
    with open('DZPhonebook.txt', 'r') as file:
        for line in file:
            text += line
            text += '\n'
        update.message.reply_text(text)