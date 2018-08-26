def new_board():
    return [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]


def position(board, row, column):
    return board[row][column]


def print_board(b):
    for i in range(3):
        row = ''
        for j in range(3):
            row += b[i][j] + ' '
        row.strip(' ')
        print(row)


def make_move(b, row, column, player):
    assert b[row][column] == '~', 'That space is already taken'
    b[row][column] = player
    return b


def col_win(b, player):
    for col in range(3):
        if position(b, 0, col) == player and position(b, 1, col) == player and position(b, 2, col) == player:
            return True
    return False


def row_win(b, player):
    for row in range(3):
        if position(b, row, 0) == player and position(b, row, 1) == player and position(b, row, 2):
            return True
    return False


def diag_win(b, player):
    if position(b, 0, 0) == player and position(b, 1, 1) == player and position(b, 2, 2) == player:
        return True
    elif position(b, 0, 2) == player and position(b, 1, 1) == player and position(b, 2, 0) == player:
        return True
    return False


def other_player(cur_player):
    if cur_player == 'X':
        return 'O'
    else:
        return 'X'


if __name__ == "__main__":
    test_board = new_board()
    test_board = make_move(test_board, 1, 1, 'X')
    test_board = make_move(test_board, 1, 0, 'O')
    test_board = make_move(test_board, 2, 0, 'O')
    test_board = make_move(test_board, 0, 0, 'X')
    test_board = make_move(test_board, 2, 2, 'X')
    print(diag_win(test_board, 'x'))
    print_board(test_board)


