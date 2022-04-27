

board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]


def game_board(main_board):
    for row in main_board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def quit(user_input):
    if user_input.lower() == 'q':
        return True


def check_input(user_input):
    try:
        val = int(user_input)
        if 9 >= val >= 1:
            return True
        print("remember that the input is between 1 and 9")
    except ValueError:
        print("That's not an int!")


while True:
    game_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    if not check_input(user_input): continue
