# Board
list_board = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']


# To show the initial board
def board_game(list_x):
    board_print = ['-', '-', '-',
                   '-', '-', '-',
                   '-', '-', '-']
    print(list_board[0], ' | ', list_board[1], ' | ', list_board[2])
    print(list_board[3], ' | ', list_board[4], ' | ', list_board[5])
    print(list_board[6], ' | ', list_board[7], ' | ', list_board[8])


print(board_game(list_board))


# To check if in the horizontal lines exists a winner combination
def horizontal(listh):
    if listh[0] == listh[1] == listh[2] == 'X':
        return True
    if listh[0] == listh[1] == listh[2] == 'O':
        return True
    elif listh[3] == listh[4] == listh[5] == 'X':
        return True
    elif listh[3] == listh[4] == listh[5] == 'O':
        return True
    elif listh[6] == listh[7] == listh[8] == 'X':
        return True
    elif listh[6] == listh[7] == listh[8] == 'O':
        return True


# To check if in the vertical lines exists a winner combination
def vertical(listv):
    if listv[0] == listv[3] == listv[6] == 'X':
        return True
    if listv[0] == listv[3] == listv[6] == 'O':
        return True
    elif listv[1] == listv[4] == listv[7] == 'X':
        return True
    elif listv[1] == listv[4] == listv[7] == 'O':
        return True
    elif listv[2] == listv[5] == listv[8] == 'X':
        return True
    elif listv[2] == listv[5] == listv[8] == 'O':
        return True


# To check if in the diagonal lines exists a winner combination
def diagonal(listd):
    if listd[0] == listd[4] == listd[8] == 'X':
        return True
    if listd[0] == listd[4] == listd[8] == 'O':
        return True
    elif listd[2] == listd[4] == listd[6] == 'X':
        return True
    elif listd[2] == listd[4] == listd[6] == '0':
        return True


# Game action
def player_action():
    active = 1
#    while active == 1:
    while True:
        print('X turn')
        v = int(input('Type the position for your X: '))
        if list_board[v] != '-':
            correct_position = 1
            while correct_position == 1:
                print('That position is already used. Try again ')
                v = int(input('Type the position for your X: '))
                if list_board[v] == '-':
                    list_board[v] = 'X'
                    correct_position = 0
                    # Check
                    if horizontal(list_board) is True:
                        print('X wins!!!')
                        break
                    #            active = 0
                    elif vertical(list_board) is True:
                        print('X wins!!!')
                        break
                    #           active = 0
                    elif diagonal(list_board) is True:
                        print('X wins!!!')
                        break
                #          active = 0
                # Check
        else:
            list_board[v] = 'X'
            print(board_game(list_board))
            # Check
            if horizontal(list_board) is True:
                print('X wins!!!')
                break
            #            active = 0
            elif vertical(list_board) is True:
                print('X wins!!!')
                break
            #           active = 0
            elif diagonal(list_board) is True:
                print('X wins!!!')
                break
        #          active = 0
        # Check

        print('0 turn')
        v = int(input('Type the position for your O: '))
        if list_board[v] != '-':
            correct_position2 = 1
            while correct_position2 == 1:
                print('That position is already used. Try again ')
                v = int(input('Type the position for your O: '))
                if list_board[v] == '-':
                    list_board[v] = 'O'
                    correct_position2 = 0
                    # Check
                    if horizontal(list_board) is True:
                        print('O wins!!!')
                        break
                    #            active = 0
                    elif vertical(list_board) is True:
                        print('O wins!!!')
                        break
                    #           active = 0
                    elif diagonal(list_board) is True:
                        print('O wins!!!')
                        break
                #          active = 0
                # Check
        else:
            list_board[v] = 'O'
            print(board_game(list_board))
            # Check
            if horizontal(list_board) is True:
                print('O wins!!!')
                break
            #            active = 0
            elif vertical(list_board) is True:
                print('O wins!!!')
                break
            #           active = 0
            elif diagonal(list_board) is True:
                print('O wins!!!')
                break
        #          active = 0
        # Check



player_action()
