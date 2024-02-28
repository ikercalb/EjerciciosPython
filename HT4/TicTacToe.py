from os import system

from Game import Game
from random import randint
import numpy as np

players = [' ', 'O', 'X']


def numeric_2_position(numeric):
    if numeric == 7:
        return 0, 0
    elif numeric == 8:
        return 0, 1
    elif numeric == 9:
        return 0, 2
    elif numeric == 4:
        return 1, 0
    elif numeric == 5:
        return 1, 1
    elif numeric == 6:
        return 1, 2
    elif numeric == 1:
        return 2, 0
    elif numeric == 2:
        return 2, 1
    elif numeric == 3:
        return 2, 2
    else:
        return -1, -1


def is_full(board):
    full = True
    for i in range(0, len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                full = False

    return full


def check_arr(array):
    eq = False
    val = array[0]
    for i in range(len(array)):
        if val != array[i]:
            break
    else:
        if val != 0:
            eq = True
    return eq


def check_rows(board):
    eq = False
    for i in range(len(board)):
        eq = check_arr(board[i])
        if eq:
            break
    return eq


def check_cols(board):
    eq = False
    for i in range(len(board[0])):
        eq = check_arr([row[i] for row in board])
        if eq:
            break
    return eq


def check_diags(board):
    eq = False
    l = len(board)
    if check_arr([board[i][i] for i in range(l)]):
        eq = True
    elif check_arr([board[l - 1 - i][i] for i in range(l - 1, -1, -1)]):
        eq = True
    return eq


def has_won(board):
    won = False
    if check_rows(board):
        won = True
    elif check_cols(board):
        won = True
    elif check_diags(board):
        won = True
    return won


class TicTacToe(Game):
    def __init__(self):
        self.first_player_idx = 0
        self.second_player_idx = 0
        self.board = []
        self.current_player = 0

    def game_init(self, config):
        self.first_player_idx = 1 if randint(0, 1) == 0 else -1
        self.second_player_idx = 1 if self.first_player_idx == -1 else -1
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = self.first_player_idx

    def game_input(self) -> str:
        return input("Enter player " + players[self.current_player] + "\n>")

    def game_turn(self, in_str):
        fil, col = numeric_2_position(int(in_str))
        if (fil == -1) & (col == -1):
            return

        if self.board[fil][col] != 0:
            return

        self.board[fil][col] = self.current_player
        self.current_player *= -1

    def game_print(self):
        _ = system('clear')
        print("############################################################")
        print("###################### TIC TAC TOE  ########################")
        print("############################################################")
        print("")
        print("                      +---+---+---+")
        print("                      | " + str(players[self.board[0][0]]) +
              " | " + str(players[self.board[0][1]]) +
              " | " + str(players[self.board[0][2]]) + " |")
        print("                      +---+---+---+")
        print("                      | " + str(players[self.board[1][0]]) +
              " | " + str(players[self.board[1][1]]) +
              " | " + str(players[self.board[1][2]]) + " |")
        print("                      +---+---+---+")
        print("                      | " + str(players[self.board[2][0]]) +
              " | " + str(players[self.board[2][1]]) +
              " | " + str(players[self.board[2][2]]) + " |")
        print("                      +---+---+---+")

    def game_is_finish(self) -> bool:
        finish = False

        if has_won(self.board):
            finish = True
        elif is_full(self.board):
            finish = True

        return finish

    def game_finish_msg(self) -> str:
        msg = "Congrats!! Player " + players[-self.current_player] + " has won"
        return msg
