from colorama import init, Fore, Back
init()
from art import logo
import itertools

print(logo)


def game_board(main_board):
    """Take any board list and display it in certain way"""
    for row in main_board:
        for slot in row:
            print(f"{slot} ", end="")
        print()
    return main_board


def first_check(board_size):
    """Make sure that the smallest board start from 2 and no string input"""
    try:
        val = int(board_size)
        if val >= 2:
            return True
        print(Fore.RED + "remember that the smallest board must by 2 * 2")
    except ValueError:
        print(Fore.RED + "That's not an int!")


def quit(exit):
    """When you want to leave a game"""
    if exit.lower() == 'q':
        return True
    return False


def check_input(user_input, slot_number):
    """The input must be number and in a certain range"""
    try:
        val = int(user_input)
        if slot_number >= val >= 1:
            return True
        print(Fore.RED + f"remember that the input is between 1 and {slot_number}")
    except ValueError:
        print(Fore.RED + "That's not an int!")


def coordinates(user_input, board):
    """Take a dynamic row and col"""
    row = int(user_input / len(board))
    col = int(user_input % len(board))
    return (row, col)


def is_taken(coord, board):
    """Check if the place is free to use"""
    row = coord[0]
    col = coord[1]
    if board[row][col] != "_":
        print(Fore.RED + "This position is been taken")
        return True


def turn_players():
    """Using an iterator to change the player"""
    player = [Fore.BLUE + "x", Fore.GREEN + "o"]
    return itertools.cycle(player)


player_choice = turn_players()


def add(player, coord, board):
    """Add a player to the free selected place"""
    row = coord[0]
    col = coord[1]
    board[row][col] = player


def win(player, board):
    """The dynamic logic of the game (horizontal, vertical and diagonal)"""

    def all_same(side):
        if side.count(side[0]) == len(side) and side[0] != "_":
            return True
        return False

    for row in board:
        if all_same(row):
            print(Fore.LIGHTCYAN_EX + f"{player.upper()} Win Horizontally --")
            return True

    for col in range(len(board)):
        vertical = []
        for row in board:
            vertical.append(row[col])
        if all_same(vertical):
            print(Fore.LIGHTYELLOW_EX + f"{player.upper()} Win Vertically |")
            return True

    diags = []
    for index in range(len(board)):
        diags.append(board[index][index])
    if all_same(diags):
        print(Fore.LIGHTMAGENTA_EX + f"{player.upper()} Win Diagonally \\")
        return True

    diags = []
    for row, col in enumerate(reversed(range(len(board)))):
        diags.append(board[row][col])
    if all_same(diags):
        print(Fore.LIGHTMAGENTA_EX + f"{player.upper()} Win Diagonally /")
        return True
    return False


def again():
    """Ask the user for another game or exit from the game"""
    again = input("Do you like to play again (Y or N): ")
    if again.upper() == "Y":
        print(Fore.YELLOW + "Reload New Game")
        return False
    elif again.upper() == "N":
        print(Fore.CYAN + "Byeeeeee To You")
        return True
    else:
        print(Fore.MAGENTA + "You typed something wrong, by-es")
        return True


play = True
while play:
    init(autoreset=True)
    # The main loop of the game (the size of the board)
    board_size = input("What size do you like the board to be Or press \"q\" to quit: ")
    if quit(board_size): break
    if not first_check(board_size): continue
    slot_number = int(board_size) ** 2
    turns = 0
    board = [["_" for j in range(int(board_size))] for i in range(int(board_size))]

    game_won = False
    while not game_won:
        # The game loop step by step
        board = game_board(board)
        user_input = input(f"Please enter a position from 1 through {slot_number} or enter \"q\" to quit: ")
        if quit(user_input):
            break
        if not check_input(user_input, slot_number):
            continue
        user_input = int(user_input) - 1
        coord = coordinates(user_input, board)
        if is_taken(coord, board):
            continue
        player = next(player_choice)
        add(player, coord, board)
        if win(player, board):
            board = game_board(board)
            if again():
                play = False
            break

        turns += 1
        if turns == slot_number:
            print(
                Back.LIGHTWHITE_EX + Fore.LIGHTMAGENTA_EX + "This Game" + Fore.LIGHTYELLOW_EX + " is A Tie" + Fore.LIGHTCYAN_EX + " X vs O")
            board = game_board(board)
            if again():
                play = False
            game_won = True