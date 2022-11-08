import telebot
bot = telebot.TeleBot('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

@bot.message_handler(command="/hi")
def hi(message):
    id = message.chat.id
    bot.send_message(id, "Hello")