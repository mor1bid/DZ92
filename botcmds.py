from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def howareu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'How bout conquering the world, {update.effective_user.first_name}?')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def summe(update: Update, context: CallbackContext) -> None:
    numa = int(input('Input first number, please: '))
    update.message.reply_text({numa})
    numb = int(input('second: '))
    update.message.reply_text({numb})