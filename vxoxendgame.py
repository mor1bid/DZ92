from virtuxox import board

if board[0, 0] == 'X' and board[2, 0] == board[1, 0] == board[0, 0] or board[0, 0] == 'X' and board[2, 2] == board[1, 1] == board[0, 0] or board[0, 0] == 'X' and board[0, 2] == board[0, 1] == board[0, 0]:
        print('Игрок 1 побеждает!')
elif board[0, 0] == 'O' and board[2, 0] == board[1, 0] == board[0, 0] or board[0, 0] == 'O' and board[2, 2] == board[1, 1] == board[0, 0] or board[0, 0] == 'O' and board[0, 2]==board[0, 1]==board[0, 0]:
        print('Игрок 2 побеждает!')
elif board[1] == 'X' and board[1, 2] == board[1, 1] == board[1, 0]:
        print('Игрок 1 побеждает!')
elif board[1] == 'O' and board[1, 2] == board[1, 1] == board[1, 0]:
    print('Игрок 2 побеждает!')
elif board[2] == 'X' and board[2, 2] == board[2, 1] == board[2, 0] or board[2, 0] == 'X' and board[0, 2] == board[1, 1] == board[2, 0]:
    print('Игрок 1 побеждает!')
elif board[2] == 'O' and board[2, 2] == board[2, 1] == board[2, 0] or board[2, 0] == 'O' and board[0, 2] == board[1, 1] == board[2, 0]:
    print('Игрок 2 побеждает!')
elif board[0, 1] == 'X' and board[2, 1] == board[1, 1] == board[0, 1]:
    print('Игрок 1 побеждает!')
elif board[0, 1] == 'O' and board[2, 1] == board[1, 1] == board[0, 1]:
    print('Игрок 2 побеждает!')
elif board[0, 2] == 'X' and board[2, 2] == board[1, 2] == board[0, 2]:
    print('Игрок 1 побеждает!')
elif board[0, 2] == 'O' and board[2, 2] == board[1, 2] == board[0, 2]:
    print('Игрок 2 побеждает!')