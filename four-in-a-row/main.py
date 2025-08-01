import utils
from board import Board

utils.clear_screen()
board = Board()
board.init_board()
board.show_board()

turn = "Player 1"

while board.check_win(1) == False and board.check_win(2) == False:
    valid = False
    while valid == False: # Keeps prompting the user until a valid value is received
        col = input(f"{turn}, insert the column you want to fill(1-7)\n")
        if col == '1' or col == '2' or col == '3' or col == '4' or col == '5' or col == '6' or col == '7':
            col = int(col) - 1
            valid = True
        else:
            valid = False
            print("Not valid!")
    if board.place(col, turn) == True:
        utils.clear_screen()
        board.show_board()
        if turn == "Player 1":
            turn = "Player 2"
        else:
            turn = "Player 1"
    else:
        utils.clear_screen()
        board.show_board()
        print("Invalid input!")

if board.check_win(1) == True:
    print("Player 1 won!")
else:
    print("Player 2 won!")