from os import system
from random import randint
from threading import Thread, Event, Lock

from Game import Game
from getkey import getkey


class MyThread(Thread):
    def __init__(self, event, game):
        Thread.__init__(self)
        self.stopped = event
        self.game = game
        self.lock = game.lock

    def run(self):
        while not self.stopped.wait(0.3):
            self.lock.acquire()

            for idx, elem in enumerate(self.game.enemies):
                if not self.game.finish:
                    new_player = [elem[0], elem[1]]
                    while not self.game.is_valid_move(new_player):
                        num = randint(0, 3)
                        if num == 0:
                            new_player = [elem[0] - 1, elem[1]]
                        elif num == 1:
                            new_player = [elem[0], elem[1] - 1]
                        elif num == 2:
                            new_player = [elem[0] + 1, elem[1]]
                        else:
                            new_player = [elem[0], elem[1] + 1]

                    self.game.enemies[idx] = new_player

                    if (self.game.player[0] == new_player[0]) and (self.game.player[1] == new_player[1]):
                        self.game.finish = True
                        self.game.stopFlag.set()

            self.lock.release()
            self.game.game_print()


class DungeonCrawl(Game):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.walls = []
        self.num_enemies = 0
        self.player = [0, 0]
        self.enemies = []
        self.finish = False

        self.stopFlag = None
        self.lock = None
        self.thread = None

    def game_init(self, config):
        self.width = int(config['Width'])
        self.height = int(config['Height'])
        pct = float(config['WallPct'])
        self.num_enemies = int(config['NumEnemies'])
        self.stopFlag = Event()
        self.lock = Lock()
        self.thread = MyThread(self.stopFlag, self)

        myset = set()
        num_walls = round(self.width * self.height * pct)
        while len(myset) < num_walls:
            fil = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            if ((fil == 0) and (col == 0)) or ((fil == (self.height - 1)) and (col == (self.width - 1))):
                continue
            myset.add((fil, col))

        self.walls = list(myset)
        self.walls.sort()

        myset = set()
        while len(myset) < self.num_enemies:
            fil = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            if ((fil == 0) and (col == 0)) or ((fil == (self.height - 1)) and (col == (self.width - 1))):
                continue
            if (fil, col) in self.walls:
                continue
            myset.add((fil, col))
        self.enemies = list(myset)
        self.enemies.sort()

        self.thread.start()

    def game_input(self) -> str:
        return getkey()

    def game_is_finish(self) -> bool:
        return self.finish

    def game_print(self):
        k = 0
        e = 0
        _ = system('clear')
        print("############################################################")
        print("##################### DUNGEON CRAWL ########################")
        print("############################################################")
        self.lock.acquire()
        print("+", end="-")
        for i in range(self.width):
            print("-", end="-")
        print("+")

        for i in range(self.height):
            print("|", end=" ")
            for j in range(self.width):
                if i == self.player[0] and j == self.player[1]:
                    print("$", end=" ")
                elif (i == self.height - 1) and (j == self.width - 1):
                    print(">", end=" ")
                elif i == 0 and j == 0:
                    print("<", end=" ")
                elif (k < len(self.walls)) and ((self.walls[k][0] == i) and (self.walls[k][1] == j)):
                    print("#", end=" ")
                    k = k + 1
                elif (e < len(self.enemies)) and ((self.enemies[e][0] == i) and (self.enemies[e][1] == j)):
                    print("@", end=" ")
                    e = e + 1
                else:
                    print(" ", end=" ")
            print("|")

        print("+", end="-")
        for i in range(self.width):
            print("-", end="-")
        print("+")
        self.lock.release()

    def is_valid_move(self, new_player):
        is_valid = False
        if 0 <= new_player[0] < self.height and 0 <= new_player[1] < self.width:
            for elem in self.walls:
                if elem[0] == new_player[0] and elem[1] == new_player[1]:
                    break
            else:
                for elem in self.enemies:
                    if elem[0] == new_player[0] and elem[1] == new_player[1]:
                        break
                else:
                    is_valid = True

        return is_valid

    def game_turn(self, in_str):
        self.lock.acquire()

        if not self.finish:
            if in_str == "w":
                new_player = [self.player[0] - 1, self.player[1]]
            elif in_str == "a":
                new_player = [self.player[0], self.player[1] - 1]
            elif in_str == "s":
                new_player = [self.player[0] + 1, self.player[1]]
            elif in_str == "d":
                new_player = [self.player[0], self.player[1] + 1]
            else:
                new_player = [self.player[0], self.player[1]]

            if self.is_valid_move(new_player):
                self.player = new_player

            if (self.player[0] == (self.height - 1)) and (self.player[1] == (self.width - 1)):
                print("Congrats!! You reached the end")
                self.finish = True
                self.stopFlag.set()
            if self.player in self.enemies:
                print("Ooops, You died!")
                self.finish = True
                self.stopFlag.set()

        self.lock.release()

    def game_finish_msg(self) -> str:
        msg = "GAME OVER"
        return msg
