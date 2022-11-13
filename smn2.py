import telebot
from spiek import *
from cmath import *
import cmath
bot = telebot.TeleBot('5479458028:AAHnAfaQe6CqI0LNVcFeSaKzXEGp0ygFhxE')

print('\nNashira s\'here')

@bot.message_handler(commands=['math'])
def math(meg: telebot.types.Message):
    with open('db.csv', 'a') as file:
        file.write(f'{meg.from_user.first_name}, {meg.from_user.id}, {meg.text} ({datetime.datetime.now().replace(microsecond=0)})\n')
    bot.send_message(meg.from_user.id, 'Hello. Please select mode by typing a proper number:\n(1) Rational\(2) Complex')
    bot.register_next_step_handler(meg, mode)

def mode(msg: telebot.types.Message, start = 0):
    if start != 0:
        bot.send_message(msg.from_user.id, 'Please select mode by typing a proper number:\n(1) Rational\(2) Complex')   
    answ = msg.text
    if answ == '1':
        bot.send_message(msg.from_user.id, 'Now input your request, please.\nIn this mode, you can sum[+], substract[-], multiply[*] or divide[/]\nany rational numbers in any order, in round brackets [()] too')
        bot.register_next_step_handler(msg, work)
    elif answ == '2':
        bot.send_message(msg.from_user.id, 'Now input your request, please.\nIn this mode, you can use:\nHyperbolic functions(acosh, asinh, atanh, cosh, sinh, tanh)\nTrigonometric functions(acos, asin, atan, cos, sin, tan)\nClassification functions(isfinite, isinf, isnan, isclose)\nLogarithmic functions(exp, log, log10, sqrt) on a single number')
        bot.register_next_step_handler(msg, calc)

def work(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'Input request')
    try:
        ask = ''
        aski = message.text.split()
        for i in aski:
            ask += i
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

        bot.reply_to(message, f'Answer: {round(count_from_string(ask), 2)}\nFor new request, type /math')
    except Exception:
        bot.reply_to(message, f'ERROR\nFor new request, type /math')

def calc(message: telebot.types.Message):
    try:
        ask = message.text.split()
        func = getattr(cmath, ask[0])
        if ask[0] == 'log' and len(ask) > 2 or ask[0] == 'rect' and len(ask) > 2:
            result = func(int(ask[1]), int(ask[2]))
        else:
            result = func(int(ask[1]))
        bot.reply_to(message, f'Answer: {round(abs(result), 2)}\nFor new request, type /math') 
    except Exception:
        bot.reply_to(message, f'ERROR\nFor new request, type /math')   

bot.polling(non_stop=True)