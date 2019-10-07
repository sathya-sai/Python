import os
import time

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")


while True:
    os.system("clear")
    print_board()

    # player X input
    choice = int(input("please choose an element space of X"))
    if board[choice] == " ":
             board[choice] = "X"
    else:
            print("Sorry,that is not empty space")
            time.sleep(1)
        # checks for X win
    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
            (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
            (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
            (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
            (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
            (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
            (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
            (board[3] == "X" and board[5] == "X" and board[7] == "X"):
            os.system("clear")
            print_board()

            print('X wins! Congrats')
            break

    os.system("clear")
    print_board()
    isFull = True
    if " " in board:
            isFull = False

    if isFull == True:
            print('Tie!')
            break

    # player O input
    choice = int(input("please choose an element space of 0"))
    if board[choice] == " ":
            board[choice] = "O"
    else:
            print("Sorry,that is not empty space")
            time.sleep(1)

    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
            (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
            (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
            (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
            (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
            (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
            (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
            (board[3] == "O" and board[5] == "O" and board[7] == "O"):

            os.system("clear")
            print_board()

            print('O wins! Congrats')
            break

    isFull = True
    if " " in board:
            isFull = False

    if isFull == True:
            print('Tie!')
            break
