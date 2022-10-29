from telegram import Update, Bot, Chat
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from pathlib import Path
import datetime
from spiek import *
user = os.path.join(os.path.expanduser('~'), 'Desktop', 'Phonebook.txt')
# home = str(Path.home())
# hpath = os.path.expanduser(f"{user}\\Desktop\\")
updater = Updater('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

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
    update.message.reply_text(f'Here ye go:\n/hello\n/howareu\n/time\n/summe\nFor work with a phonebook, type:\n/nlist [text] - to write a note in long list.\n/nline [text] - to write a note in single line\n/nread [path] - to view chosed file\'s exterier\n/nimport [path] - to move data from another file into your phonebook\n/nexport [path] - to move book\'s data into another file\n')

def makenote1 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(f'{user}', 'a') as file:
        for i in msg:
            file.write(' \n')
            file.write(i)
        file.write(' \n') 
        update.message.reply_text(f'{user}\nDone. For readin your notes, type /nread and path to your file')
def makenote2 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(f'{user}', 'a') as file:
        file.write(' \n')
        for i in msg:
            file.write(i)
            file.write(' ')
        file.write(' \n')
        update.message.reply_text(f'{user}\nDone. For readin your notes, type /nread and path to your file')

def readnote (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    text = ''
    # msg = update.message.text
    with open(path, 'r') as file:
        for line in file:
            text += line
            text += '\n'
        update.message.reply_text(text)

def exportnote (update: Update, context: CallbackContext):
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open('Phonebook.txt', 'r') as expex:
        exp = expex.readlines()
    with open(path, 'a') as file:
        file.write(' \n')
        file.writelines(exp)
    update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

def importnote (update: Update, context: CallbackContext):
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
    update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

# def math(update: Update, context: CallbackContext):