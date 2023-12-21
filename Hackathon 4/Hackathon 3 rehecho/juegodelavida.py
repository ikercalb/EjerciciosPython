import random
import time


import numpy as np

DEFAULT_CELL_WIDTH = 10
DEFAULT_CELL_HEIGHT = 10
DEFAULT_CELL_INIT_ALIVE_CELL_NUM = 50
DEFAULT_CELL_GAME_TURNS = 10
ALIVE = "🦠 "
DEAD = " . "


class juegodelavida:
    def __init__(self, width=DEFAULT_CELL_WIDTH, height=DEFAULT_CELL_HEIGHT,
                 init_alive_cell_num=DEFAULT_CELL_INIT_ALIVE_CELL_NUM, game_turns=DEFAULT_CELL_GAME_TURNS):
        self.width = width
        self.height = height
        self.init_alive_cell_num = init_alive_cell_num
        self.game_turns = game_turns
        self.cells = np.zeros((self.height, self.width), dtype=bool)

    def draw_grid(self):
        print("@@@@     |---     @        @              ")
        print("@        |--      @        @              ")
        print("@@@@     |---     @@@@     @@@@           ")
        for i in range(self.height):
            for j in range(self.width):

                if self.cells[i][j]:
                    print(ALIVE, end='')
                    self.cells[i][j] = 1
                else:
                    print(DEAD, end='')
                    self.cells[i][j] = 0
            print()

    def set_init_alive_cells(self):
        myset = set()

        while len(myset) < self.init_alive_cell_num:
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            myset.add((x, y))

        for elem in myset:
            self.cells[elem[0]][elem[1]] = True

    def next_turn_grid(self):
        new_grid = self.cells.copy()
        for i in range(self.height):
            for j in range(self.width):
               vecinos = self.get_cell_living_neighbors(i, j)

               if self.cells[i][j]:
                    if vecinos < 2 or vecinos > 3:
                        new_grid[i][j] = False
                    else:
                        new_grid[i][j] = True
               else:
                    if vecinos == 3:
                        new_grid[i][j] = True

        self.cells = new_grid

    def get_cell_living_neighbors(self, fil, col):
        count = 0
        for i in range(fil - 1, fil + 2):
            for j in range(col - 1, col + 2):
                if (i < 0) or (j < 0) or (i >= self.height) or (j >= self.width) or ((i == fil) and (j == col)):
                    continue
                if self.cells[i][j]:
                    count = count + 1
        return count

    def wait(self):
        time.sleep(0.5)

    def init_game(self):
        finish = False
        while not finish:
            self.next_turn_grid()
            self.draw_grid()
            self.wait()