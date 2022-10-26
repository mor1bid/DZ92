from tictactoe import *
from tictactoe.egtb import *

print('1. Крестики-нолики! \nВводите соответсвующую позицию в горизонтали и вертикали для игры. \nПервый ряд, первый столбец: 0 0\nВторой ряд, первый столбец: 0 1\nТретий ряд, второй столбец: 1 2 и т.д.')
board = Board(dimensions = (3, 3, 1), x_in_a_row = 8)
print(board)
for i in range(0, 10):
    if i % 2 != 0:
        xy = input('\nИгрок 2, введите желаемую позицию: ').split()
    else: 
        xy = input('\nИгрок 1, введите желаемую позицию: ').split()
    board.push((int(xy[0]), int(xy[1])))
    print(board)