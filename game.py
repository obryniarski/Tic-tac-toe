print('hello world!')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


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


test_board = new_board()
test_board = make_move(test_board, 1, 1, 'X')
test_board = make_move(test_board, 1, 0, 'O')
test_board = make_move(test_board, 0, 0, 'O')
test_board = make_move(test_board, 2, 0, 'O')
print(col_win(test_board, 'O'))
print_board(test_board)