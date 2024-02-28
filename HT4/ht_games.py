from os import system
import time
from TicTacToe import TicTacToe
from DungeonCrawl import DungeonCrawl
from GameOfLife import GameOfLife
from Snake import Snake

import configparser

configuration = configparser.ConfigParser()
configuration.read('config.ini')


def print_menu():
    _ = system('clear')
    print("############################################################")
    print("#################### HACKATON GAMES ########################")
    print("############################################################")
    print("Select Game:")
    print("  1. Tic-Tac-Toe")
    print("  2. Dungeon Crawl")
    print("  3. Conway's Game of Life")
    print("  4. Snake")
    print("  0. EXIT")
    print()
    print()
    print()


finish = False

while not finish:
    print_menu()
    ch = (input(">"))

    if ch == "1":
        gm = TicTacToe()
        conf = configuration['TicTacToe']
    elif ch == "2":
        gm = DungeonCrawl()
        conf = configuration['DungeonCrawl']
    elif ch == "3":
        gm = GameOfLife()
        conf = configuration['GameOfLife']
    elif ch == "4":
        gm = Snake()
        conf = configuration['Snake']
    else:
        finish = True
        continue

    gm.game_init(conf)
    gm.game_print()
    while not gm.game_is_finish():
        gm.game_turn(gm.game_input())
        gm.game_print()

    print(gm.game_finish_msg())
    time.sleep(1)
