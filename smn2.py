import telebot
from spiek import *
from cmath import *

def calc():
    import math
    myfunc = input('Enter a function: ')
    num = float(input('Enter a number: '))
    func = getattr(math, myfunc)
    result = func(num)
    return result

a=calc()
print (a)

bot = telebot.TeleBot('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

print('\nit\'s me, MARIO!')

@bot.message_handler(commands=['math'])
def math(meg: telebot.types.Message):
    with open('db.csv', 'a') as file:
        file.write(f'{meg.from_user.first_name}, {meg.from_user.id}, {meg.text} ({datetime.datetime.now().replace(microsecond=0)})\n')
    bot.send_message(meg.from_user.id, 'Go ahead, porcupine')
    bot.register_next_step_handler(meg, work)

def work(message: telebot.types.Message):
    ask = message.text
    def minus(ask):
        return ask[0] - ask[1]

    def multi(ask):
        return ask[0] * ask[1]

    def divide(ask):
        return ask[0] / ask[1]

    def count_from_string(ask):
        if "(" in ask:
            bk1 = ask.rindex("(")
            bk2 = ask.index(")", bk1)
            return count_from_string(ask[:bk1] + str(count_from_string(ask[bk1 + 1:bk2])) + ask[bk2 + 1:])
        if ask.isdigit():
            return int(ask)
        if "+" in ask:
            return sum([count_from_string(item) for item in ask.split("+", 1)])
        if "-" in ask:
            return minus([count_from_string(item) for item in ask.split("-", 1)])
        if "/" in ask:
            return divide([count_from_string(item) for item in ask.split("/", 1)])
        if "*" in ask:
            return multi([count_from_string(item) for item in ask.split("*", 1)])

    bot.send_message(message.from_user.id, f'Answer: {round(count_from_string(ask), 2)}')
# @bot.message_handler(commands=["hi"])
# def hi(message: telebot.types.Message):
#     bot.send_message(message.from_user.id, "Hello")

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # Если сообщение из чата с ботом
#     if call.message:
#         if call.data == "test":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
#     # Если сообщение из инлайн-режима
#     elif call.inline_message_id:
#         if call.data == "test":
#             bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

bot.polling(non_stop=True)