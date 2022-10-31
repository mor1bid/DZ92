from telegram import Update
from telegram.ext import CallbackContext
prog = 0
while prog == 0:
    ask = input('Введите желаемый запрос: \n')
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
        if ":" in msg:
            return divide([count_from_string(item) for item in msg.split("/", 1)])
        if "*" in msg:
            return multi([count_from_string(item) for item in msg.split("*", 1)])

    print(f'Ответ: {count_from_string(msg)}')
    # qi = 0
    # while qi == 0:
    #     q = (input('Новый запрос? y/n: '))
    #     if q == 'n':
    prog += 1
    #         qi += 1
    #     elif q == 'y':
    #         qi += 1
    #     else:
    #         print('Ошибка!')