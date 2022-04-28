import itertools

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


def is_taken(player, coord, board):
    row = coord[0]
    col = coord[1]
    if board[row][col] != "_":
        print("This position is been taken")
        return True
    else:
        board[row][col] = player


def coordinates(user_input, board):
    row = int(user_input / len(board))
    col = int(user_input % len(board))
    return (row,col)

def turn_players():
    player = ["x", "o"]
    return itertools.cycle(player)


player_choice = turn_players()



def win(player, board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "_":
            print(f"{player.upper()} Win Horizontally")
            return True


    for col in range(len(board)):
        vertical = []
        for row in board:
            vertical.append(row[col])
        if vertical.count(vertical[0]) == len(vertical) and vertical[0] != "_":
            print(f"{player.upper()} Win Vertically |")
            return True







while True:
    game_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    if not check_input(user_input): continue
    user_input = int(user_input) - 1
    coord = coordinates(user_input, board)
    player = next(player_choice)
    if is_taken(player, coord, board): continue
    if win(player, board):
        game_board(board)
        break
