from telepot import *
from telegram import Update
from telegram.ext import CallbackContext
import os
import datetime
from spiek import *
if not os.path.exists(os.path.expanduser('~/NSHR')):
    os.makedirs(os.path.expanduser('~/NSHR'))
home = os.path.join(os.path.expanduser('~/NSHR'), 'Phonebook.txt')

def howareu(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'How bout conquering the world, {update.effective_user.first_name}?')

def hello(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def summe(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    digs = msg.split()
    numa = int(digs[1])
    numb = int(digs[2])
    update.message.reply_text(f'Here ye go: {numb} + {numa} = {numb+numa}')

def mytime(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Its {datetime.datetime.now().time()}')

def helpme(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Here ye go:\n/hello\n/howareu\n/time\n/summe\nFor work with a phonebook, type:\nMain file path: {home}\n/nlist "text" - to write a note in main file in long list.\n/nline "text" - to write a note in main file in single line\n/ndel "file directory" - to erase all of chosen file\'s data\n/nread "file directory" - to view chosen file\'s interior\n/nload - to download main file from server\n/nimport "file directory" - to move data from another file into your phonebook\n/nexport "file directory" - to move book\'s data into another file\create new file\n')

def makenote1 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(home, 'a', encoding='UTF-8') as file:
        for i in msg:
            file.write(' \n')
            file.write(i)
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread and path to your file')
def makenote2 (update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text.split()
    msg.pop(0)
    with open(home, 'a', encoding='UTF-8') as file:
        file.write(' \n')
        for i in msg:
            file.write(i)
            file.write(' ')
        file.write(' \n')
        update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

def nload (update: Update, context: CallbackContext):
    with open(home, 'rb') as doc:
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
    with open(path, 'r', encoding='UTF-8') as file:
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
    with open(home, 'r', encoding='UTF-8') as expex:
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
    with open(home, 'a', encoding='UTF-8') as file:
        file.write('\n')
        file.writelines(imp)
    update.message.reply_text('Done. For readin your notes, type /nread and path to your file')

# def math(update: Update, context: CallbackContext):