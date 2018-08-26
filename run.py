import game


def play():
    cur_player = input('Would you like to be X or O: ').upper()
    main_board = game.new_board()

    while True:
        game.print_board(main_board)
        move_str = input('Where would you like to place an %s? (e.g. 12 for 1st row, 2nd column) ' % cur_player)
        move_row = int(move_str[0]) - 1
        move_col = int(move_str[1]) - 1
        main_board = game.make_move(main_board, move_row, move_col, cur_player)
        if game.any_win(main_board, cur_player):
            game.print_board(main_board)
            print('Congratulations Player %s! Better luck next time player %s' % (cur_player, game.other_player(cur_player)))
            break
        elif game.board_full(main_board):
            game.print_board(main_board)
            print('No more moves possible. The game ended in a draw.')
            break
        cur_player = game.other_player(cur_player)

    if input('Would you like to play again? [y/n]') == 'y':
        play()
    else:
        print('Thanks for playing.')
        return 0


play()
