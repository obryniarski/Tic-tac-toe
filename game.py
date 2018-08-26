print('hello world!')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def new_board():
    placeholder = '~'
    row = [placeholder, placeholder, placeholder]
    return [row, row, row]


def position(board, row, column):
    return board[row][column]


def print_board(b):
    for i in range(3):
        row = ''
        for j in range(3):
            row += b[i][j] + ' '
        row.strip(' ')
        print(row)


test_board = new_board()
print_board(test_board)