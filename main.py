import numpy as np
game_on = True

keys = {
    'A1': [0, 0],
    'A2': [1, 0],
    'A3': [2, 0],
    'B1': [0, 1],
    'B2': [1, 1],
    'B3': [2, 1],
    'C1': [0, 2],
    'C2': [1, 2],
    'C3': [2, 2],
    }


def generate_board():
    text = [[" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]]
    text = np.array(text)
    board = text[0].reshape((3, 3))
    return board


def check_input(user_input, symbol):
    if user_input in keys:
        position = keys[user_input]
        if game[position[0], position[1]] == ' ':
            game[position[0], position[1]] = symbol
            return 1
        else:
            print('Position already taken!')
            return 0
    else:
        print(f'{user_input} is not valid!')
        return 0


def check_endgame(board):
    # Check Rows
    for i in board:
        if ' ' not in i:
            if i[0] == i[1] == i[2]:
                return True
    # Check Columns
    columns = np.transpose(board)
    for i in columns:
        if ' ' not in i:
            if i[0] == i[1] == i[2]:
                return True
    # Check Diagonal
    if board[0, 0] != ' ' and board[0, 0] == board[1, 1] == board[2, 2]:
        return True
    elif board[0, 2] != ' ' and board[0, 2] == board[1, 1] == board[2, 0]:
        return True


game = generate_board()
turn = 1
while game_on:
    print("   A   B   C")
    print(game)
    if turn % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    user_input = input(f"{player}'s turn! Choose your placement (ex. B2)\n").upper()
    turn_successful = check_input(user_input, player)
    turn += turn_successful
    if check_endgame(game) or turn > 9:
        game_on = False
        print(game)
        if not check_endgame(game) and turn > 9:
            print("its a draw!")
        else:
            print(f'The Game is over! "{player}" wins!')

