

board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]


def game_board(main_board):
    for row in main_board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


game_board(board)





while True:
    game_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
