import utils
from board import Board

utils.clear_screen()

while True:
    isBot = input("Select game mode(duo/bot)")
    if isBot == "duo":
        isBot = False
        break
    elif isBot == "bot":
        isBot = True
        break
    else:
        print("Not valid!")

board = Board()
board.init_board()
board.show_board()

turn = "Player 1"

if isBot == False:
    while board.check_win(1) == False and board.check_win(2) == False:
        while True: # Keeps prompting the user until a valid value is received
            col = input(f"{turn}, insert the column you want to fill(1-7)\n")
            if col in ['1', '2', '3', '4', '5', '6', '7']:
                col = int(col) - 1
                break
            else:
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
else:
    while board.check_win(1) == False and board.check_win(2) == False:
        if turn == "Player 1":
            while True: # Keeps prompting the user until a valid value is received
                col = input(f"{turn}, insert the column you want to fill(1-7)\n")
                if col in ['1', '2', '3', '4', '5', '6', '7']:
                    col = int(col) - 1
                    break
                else:
                    print("Not valid!")
        else:
            col = board.bot_place()
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
        print("Player Bot won!")