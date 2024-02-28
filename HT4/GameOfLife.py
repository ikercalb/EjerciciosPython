import time
from os import system
from random import randint
import numpy as np
from Game import Game


class GameOfLife(Game):

    def __init__(self):
        self.width = 0
        self.height = 0
        self.init_alive_cells_num = 0
        self.game_turns = 0
        self.cells = []
        self.current_turn = 0
        self.alive = ""
        self.dead = ""
        self.turn_time = 0

    def game_init(self, config):
        self.width = int(config['Width'])
        self.height = int(config['Height'])
        self.init_alive_cells_num = int(config['InitAliveCells'])
        self.game_turns = int(config['Turns'])
        self.alive = config['AliveChar']
        self.dead = config['DeadChar']
        self.turn_time = float(config['TurnTime'])

        self.cells = np.zeros([self.height, self.width], dtype=bool)
        self.current_turn = 0

        my_set = set()
        while len(my_set) < self.init_alive_cells_num:
            fil = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            my_set.add((fil, col))

        for (fil, col) in my_set:
            self.cells[fil][col] = True

    def game_input(self) -> str:
        time.sleep(self.turn_time)
        return "NoNeed"

    def game_turn(self, in_str):
        self.current_turn = self.current_turn + 1
        if self.current_turn <= self.game_turns:
            self.next_turn_grid()

    def game_print(self):
        _ = system('clear')
        print("############################################################")
        print("###################### GAME OF LIFE ########################")
        print("############################################################")
        print(" TURN: ", str(self.current_turn))
        print()
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j]:
                    print(self.alive, end=" ")
                else:
                    print(self.dead, end=" ")
            print()
        print()
        print()

    def game_is_finish(self) -> bool:
        finish = False
        if self.current_turn > self.game_turns:
            finish = True
        return finish

    def next_turn_grid(self):
        new_grid = self.cells.copy()
        for i in range(self.height):
            for j in range(self.width):
                living_neighbors = self.__get_cell_living_neighbors(i, j)
                if self.cells[i][j]:  # Alive cell
                    if living_neighbors < 2 or living_neighbors > 3:
                        new_grid[i][j] = False
                else:  # Dead cell
                    if living_neighbors == 3:
                        new_grid[i][j] = True
        self.cells = new_grid

    def __get_cell_living_neighbors(self, fil, col):
        count = 0
        for i in range(fil - 1, fil + 2):
            for j in range(col - 1, col + 2):
                if (i < 0) or (j < 0) or (i >= self.height) or (j >= self.width) or ((i == fil) and (j == col)):
                    continue
                if self.cells[i][j]:
                    count = count + 1
        return count

    def game_finish_msg(self) -> str:
        msg = ""
        return msg
