from tictactoe import *
from tictactoe.egtb import *
import functools, operator

print('1. Крестики-нолики! \nВводите через пробел соответсвующую позицию в вертикали и горизонтали для игры. \nПервый ряд, первый столбец: 0 0\nВторой ряд, первый столбец: 0 1\nТретий ряд, второй столбец: 1 2 и т.д.\n')
board = Board(dimensions = (3, 3, 1), x_in_a_row = 8)
print(board)
for i in range(0, 9):
    if i % 2 != 0:
        xy = input('\nИгрок 2, введите желаемую позицию: ').split()
    else: 
        xy = input('\nИгрок 1, введите желаемую позицию: ').split()
    if i >= 5:
        dimensions = (3, 3, 1)
        total_squares = functools.reduce(operator.mul, dimensions)
        for index in reversed(range(total_squares + 1)):
            Generator(dimensions, 3, index)
            reader = Reader((3, 3, 1), 3, 9)
            print(reader.index(board))
    board.push((int(xy[0]), int(xy[1])))
    print(board)

# dimensions = (3, 3, 1)
# total_squares = functools.reduce(operator.mul, dimensions)
# for index in reversed(range(total_squares + 1)):
#     Generator(dimensions, 3, index)

# reader = Reader((3, 3, 1), 3, 9)
# print(reader.index(board))