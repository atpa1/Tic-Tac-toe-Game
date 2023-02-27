import random
import time

board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
X = chr(88)
O = chr(79)


def first_board():
    """first board display when starting the game"""
    print(" Welcome to Tic Tac Toe Game")
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# random choice who start the game.
on = True
while on:
    try:
        start_game = int(input("Choose 1 for heads or 2 for tails to start the game: "))
        if start_game == 1 or start_game == 2:
            on = False
    except KeyboardInterrupt:
        pass
    except ValueError:
        pass


def game_conditions():
    """game  board options to win or lose"""
    if board[1] + board[2] + board[3] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[1] + board[2] + board[3] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[1] + board[5] + board[9] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[1] + board[5] + board[9] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[1] + board[4] + board[7] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[1] + board[4] + board[7] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[2] + board[5] + board[8] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[2] + board[5] + board[8] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[3] + board[6] + board[9] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[3] + board[6] + board[9] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[3] + board[5] + board[7] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[3] + board[5] + board[7] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[4] + board[5] + board[6] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[4] + board[5] + board[6] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True
    if board[7] + board[8] + board[9] == 3 * chr(88):
        print("You Win, Game Over!")
        return True
    else:
        if board[7] + board[8] + board[9] == 3 * chr(79):
            print("You Lose, Game Over!")
            return True


def player_turn():
    """player's turn """
    # check player's choice number for duplication or occupied boxes
    check_player_number = True
    while check_player_number:
        try:
            box_n = int(input("Your turn, please choose box number: "))
            if O == board[box_n]:
                print(" This box is already occupied")
            elif X == board[box_n]:
                print(" You already chose this box")
            else:
                board[box_n] = X
                check_player_number = False
        # check for invalid number or character
        except IndexError:
            print(" invalid number! ")
        except ValueError:
            print(" invalid character! ")


def pc_player_turn():
    """computer's turn"""
    print("Computer turn")
    # check pc player choice number for duplication or occupied boxes
    check_pc_player_number = True
    while check_pc_player_number:
        PC_player = random.randint(1, 9)
        if X in board[PC_player] or O in board[PC_player]:
            PC_player = random.randint(1, 9)
        else:
            board[PC_player] = O
            check_pc_player_number = False
    time.sleep(3)


def game():
    """game table and players choices"""
    random_start_game = random.randint(1, 2)
    turn_count = 0
    game_on = True
    while game_on:
        if start_game == random_start_game:
            player_turn()
            print(" %c | %c | %c " % (board[1], board[2], board[3]))
            print("___|___|___")
            print(" %c | %c | %c " % (board[4], board[5], board[6]))
            print("___|___|___")
            print(" %c | %c | %c " % (board[7], board[8], board[9]))
            print("   |   |   ")
            turn_count += 1
            if game_conditions():
                game_on = False
            elif turn_count == 5:
                print("No Winner, Game Over!")
                game_on = False
            else:
                pc_player_turn()
                print(" %c | %c | %c " % (board[1], board[2], board[3]))
                print("___|___|___")
                print(" %c | %c | %c " % (board[4], board[5], board[6]))
                print("___|___|___")
                print(" %c | %c | %c " % (board[7], board[8], board[9]))
                print("   |   |   ")
                if game_conditions():
                    game_on = False
        else:
            pc_player_turn()
            print(" %c | %c | %c " % (board[1], board[2], board[3]))
            print("___|___|___")
            print(" %c | %c | %c " % (board[4], board[5], board[6]))
            print("___|___|___")
            print(" %c | %c | %c " % (board[7], board[8], board[9]))
            print("   |   |   ")
            turn_count += 1
            if game_conditions():
                game_on = False
            elif turn_count == 5:
                print("No Winner, Game Over!")
                game_on = False
            else:
                player_turn()
                print(" %c | %c | %c " % (board[1], board[2], board[3]))
                print("___|___|___")
                print(" %c | %c | %c " % (board[4], board[5], board[6]))
                print("___|___|___")
                print(" %c | %c | %c " % (board[7], board[8], board[9]))
                print("   |   |   ")
                if game_conditions():
                    game_on = False


first_board()
game()
