from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def howareu(update: Update, context: CallbackContext):
    update.message.reply_text(f'How bout conquering the world, {update.effective_user.first_name}?')

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def summe(update: Update, context: CallbackContext):
    # update.message.reply_text(f'Enter 2 digits please:')
    msg = update.message.text
    digs = msg.split()
    numa = int(digs[1])
    numb = int(digs[2])
    update.message.reply_text({numb}+{numa}, '=', {numb+numa})

def time(update: Update, context: CallbackContext):
    update.message.reply_text(f'Its {datetime.datetime.now().time()}')

def helpme(update: Update, context: CallbackContext):
    update.message.reply_text(f'Here ye go:\n/hi\n/howareu\n/time\n/summe\n')