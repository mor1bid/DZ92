from calc import minus, divide, multi
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spiek import *
from makenote-m1 import *

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
    update.message.reply_text('Done. For readin your notes, type /nread')

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
    update.message.reply_text('Done. For readin your notes, type /nread')

def math(update: Update, context: CallbackContext):
    msg = update.message.text.strip(" ")
    def minus(lst):
        return lst[0] - lst[1]

    def multi(lst):
        return lst[0] * lst[1]

    def divide(lst):
        return lst[0] / lst[1]

    def count_from_string(msg):
        if "(" in msg:
            bk1 = msg.rindex("(")
            bk2 = msg.index(")", bk1)
            return count_from_string(msg[:bk1] + str(count_from_string(msg[bk1 + 1:bk2])) + msg[bk2 + 1:])
        if msg.isdigit():
            return int(msg)
        if "+" in msg:
            return sum([count_from_string(item) for item in msg.split("+", 1)])
        if "-" in msg:
            return minus([count_from_string(item) for item in msg.split("-", 1)])
        if "/" in msg:
            return divide([count_from_string(item) for item in msg.split("/", 1)])
        if "*" in msg:
            return multi([count_from_string(item) for item in msg.split("*", 1)])
    update.message.reply_text(f'The answer is: {count_from_string(msg)}')
