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
    update.message.reply_text(f'Here ye go:\n/hi\n/howareu\n/time\n/summe\n/makenote\n/readnote\nFor work with a phonebook type:\n/nwrite\n/nread\n/nimport\n/nexport\n')

def makenote (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open('Phonebook.txt', 'a') as file:
        for i in msg:
            file.write(' \n')
            file.write(i)
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread')

def readnote (update: Update, context: CallbackContext):
    log(update, context)
    text = ''
    # msg = update.message.text
    with open('Phonebook.txt', 'r') as file:
        for line in file:
            text += line
            text += '\n'
        update.message.reply_text(text)

def importnote (update: Update, context: CallbackContext):
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open('Phonebook.txt', 'r') as expex:
        exp = expex.readlines()
    with open(path, 'a') as file:
        file.write('\n')
        file.writelines(exp)
    update.message.reply_text('Done. For readin your notes, type /nread')

def exportnote (update: Update, context: CallbackContext):
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open(path, 'r') as impex:
        imp = impex.readlines()
    with open('Phonebook.txt', 'a') as file:
        file.write('\n')
        file.writelines(imp)
    update.message.reply_text('Done. For readin your notes, type /nread')
