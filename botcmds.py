# from calc import *
from telepot import *
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler
import os
import datetime
from spiek import *
if not os.path.exists(os.path.expanduser('~\\NSHR')):
    os.makedirs(os.path.expanduser('~\\NSHR'))
home = os.path.join(os.path.expanduser('~\\NSHR'))

def howareu(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'How bout conquering the world, {update.effective_user.first_name}?')

def hello(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def mytime(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Its {datetime.datetime.now().time()}')

def helpme(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Here ye go:\n/hello\n/howareu\n/time\n/math "request"\nFor work with a phonebook, type:\nWorking path: {home}\n/nlist "text" - to write a note in main file in long list.\n/nline "text" - to write a note in main file in single line\n/ndel "file directory" - to erase all of chosen file\'s data\n/nread "file directory" - to view chosen file\'s interior\n/nload - to download main file from server\n/nimport "file directory" - to move data from another file into your phonebook\n/nexport "file directory" - to move book\'s data into another file\create new file\n')

def makenote1 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(f'{home}\\Phonebook.txt', 'a', encoding='UTF-8') as file:
        for i in msg:
            file.write(' \n')
            file.write(i)
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread and path to your file')
def makenote2 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(f'{home}\\Phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(' \n')
        for i in msg:
            file.write(i)
            file.write(' ')
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

def nload (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open(f'{home}\\{path}', 'rb') as doc:
        update.message.reply_text('Here ye go:')
        context.bot.send_document(chat_id = update.effective_chat.id, document = doc)

def ndel (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open(path, 'w', encoding='UTF-8') as file:
        file.seek(0)
        file.truncate()
        update.message.reply_text('Done.')
    
def readnote (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    text = ''
    with open(f'{home}\\{path}', 'r', encoding='UTF-8') as file:
        for line in file:
            text += line
            text += '\n'
        update.message.reply_text(text)

def exportnote (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open(f'{home}\\Phonebook.txt', 'r', encoding='UTF-8') as expex:
        exp = expex.readlines()
    with open(f'{home}\\{path}', 'a') as file:
        file.write(' \n')
        file.writelines(exp)
    update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

def importnote (update: Update, context: CallbackContext):
    log(update, context)
    path = ''
    msg = update.message.text.split()
    msg.pop(0)
    for i in msg:
        path += i
    with open(f'{home}\\{path}', 'r') as impex:
        imp = impex.readlines()
    with open(f'{home}\\Phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write('\n')
        file.writelines(imp)
    update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

def math(update: Update, context: CallbackContext):
    log(update, context)
    ask = update.message.text.split()
    ask.pop(0)
    update.message.reply_text(f'Answer: {ask}')
    msg = ''
    for i in ask:
        msg += i

    def minus(msg):
        return msg[0] - msg[1]

    def multi(msg):
        return msg[0] * msg[1]

    def divide(msg):
        return msg[0] / msg[1]

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

    update.message.reply_text(f'Answer: {round(count_from_string(msg), 2)}')