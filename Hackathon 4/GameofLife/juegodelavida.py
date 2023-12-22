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
