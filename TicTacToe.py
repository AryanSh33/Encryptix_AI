import numpy as np
import random
tboard = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
Game = True
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-------------")
    print("\n")

def player_move(board):
    inp = int(input("Enter a number from 1 to 9 for X: "))
    if inp == 1 or inp == 2 or inp == 3:
        if board[0][inp-1] == "X" or board[0][inp-1] == "O":
            print("Place already occupied")
            player_move(board)
        else:
            board[0][inp-1] = "X"
    if inp == 4 or inp == 5 or inp == 6:
        if board[1][inp-4] == "X" or board[1][inp-4] == "O":
            print("Place already occupied")
            player_move(board)
        else:
            board[1][inp-4] = "X"
    if inp == 7 or inp == 8 or inp == 9:
        if board[2][inp-7] == "X" or board[2][inp-7] == "O":
            print("Place already occupied")
            player_move(board)
        else:
            board[2][inp-7] = "X"
    return board

def computer_move(board):
    # input
    inp = random.randint(1, 9) 
    if inp == 1 or inp == 2 or inp == 3:
        if board[0][inp - 1] == "X" or board[0][inp - 1] == "O":
           
            computer_move(board)
        else:
            board[0][inp - 1] = "O"
    if inp == 4 or inp == 5 or inp == 6:
        if board[1][inp - 4] == "X" or board[1][inp - 4] == "O":
         
            computer_move(board)
        else:
            board[1][inp - 4] = "O"
    if inp == 7 or inp == 8 or inp == 9:
        if board[2][inp - 7] == "X" or board[2][inp - 7] == "O":
         
            computer_move(board)
        else:
            board[2][inp - 7] = "O"
    return board


def check_win_horizontal(board):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
        if board[0][0] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    if (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        if board[1][0] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    if (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        if board[2][0] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    else:
        return True


def check_win_vertical(board):
    if (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        if board[0][0] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    if (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        if board[0][1] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    if (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        if board[0][2] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    else:
        return True

def check_win_diagonal(board):
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        if board[0][0] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    if (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X") or (board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O"):
        if board[0][2] == "X":
            print("Player X won")
        else:
            print("Player O won")
        return False
    else:
        return True

def check_tie(board):
    if "-" not in board:
        print("It's a tie")
        return False
    else:
        return True

if __name__ == '__main__':
    print_board(tboard)
    while Game:
        tboard = player_move(tboard)
        print_board(tboard)
        if not check_win_horizontal(tboard) or not check_win_vertical(tboard) or not check_win_diagonal(tboard) or not check_tie(tboard):
            break
        print("Computers turn =>")
       
        tboard = computer_move(tboard)
        print_board(tboard)
        if not check_win_horizontal(tboard) or not check_win_vertical(tboard) or not check_win_diagonal(tboard) or not check_tie(tboard):
            break
