from os import system
from random import randint
import bisect
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
        while not self.stopped.wait(0.5):

            self.lock.acquire()
            if not self.game.finish:
                if self.game.check_if_dead():
                    print("Ooops, You died!")
                    self.game.finish = True
                    self.lock.release()
                    continue

                self.game.move()

                if self.game.check_if_food():
                    self.game.feed = True
                    self.game.generate_food()

            self.lock.release()
            self.game.game_print()


class Snake(Game):
    def __init__(self):
        self.width = 0
        self.height = 0

        self.tail = []
        self.print_tail = []
        self.head = [0, 0]
        self.food = [1, 1]
        self.direction = 0
        self.finish = False
        self.feed = False

        self.stopFlag = None
        self.lock = None
        self.thread = None

    def move(self):
        if self.feed:
            self.feed = False
        else:
            elem = self.tail.pop(-1)
            self.print_tail.remove(elem)

        self.tail.insert(0, [self.head[0], self.head[1]])
        bisect.insort(self.print_tail, [self.head[0], self.head[1]])

        if (self.direction % 4) == 1:
            self.head = [self.head[0], self.head[1] + 1]
        elif (self.direction % 4) == 2:
            self.head = [self.head[0] + 1, self.head[1]]
        elif (self.direction % 4) == 3:
            self.head = [self.head[0], self.head[1] - 1]
        else:
            self.head = [self.head[0] - 1, self.head[1]]

    def check_if_food(self) -> bool:
        return (self.head[0] == self.food[0]) and (self.food[1] == self.head[1])

    def check_if_dead(self) -> bool:
        if ((self.head[0] < 0)
                or (self.head[1] < 0)
                or (self.head[0] >= self.height)
                or (self.head[1] >= self.width)
                or (self.head in self.tail)):
            return True
        else:
            return False

    def game_init(self, config):
        self.width = int(config['Width'])
        self.height = int(config['Height'])

        self.stopFlag = Event()
        self.lock = Lock()
        self.thread = MyThread(self.stopFlag, self)

        fil = randint(0, self.height - 1)
        col = randint(0, self.width - 1)
        self.head = [fil, col]
        self.food = [fil, col]

        self.direction = randint(0, 3)
        self.__generate_tail()
        self.generate_food()

        self.thread.start()

    def generate_food(self):
        while (self.food[0] == self.head[0] and self.food[1] == self.head[1]) or (self.food in self.tail):
            fil = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            self.food = [fil, col]

    def __generate_tail(self):
        dir = self.direction
        tail_cord = [self.head[0], self.head[1]]

        while len(self.tail) < 4:
            if (dir % 4) == 1:
                tail_cord = [tail_cord[0], tail_cord[1] - 1]
            elif (dir % 4) == 2:
                tail_cord = [tail_cord[0] - 1, tail_cord[1]]
            elif (dir % 4) == 3:
                tail_cord = [tail_cord[0], tail_cord[1] + 1]
            else:
                tail_cord = [tail_cord[0] + 1, tail_cord[1]]

            if ((tail_cord[0] < 0)
                    or (tail_cord[1] < 0)
                    or (tail_cord[0] >= self.height)
                    or (tail_cord[1] >= self.width)):
                dir += 1
                continue

            self.tail.append(tail_cord)

        self.print_tail = self.tail.copy()
        self.print_tail.sort()

        print(self.tail)
        print(self.print_tail)

    def game_input(self) -> str:
        return getkey()

    def game_is_finish(self) -> bool:
        return self.finish

    def game_print(self):
        k = 0
        self.lock.acquire()
        if not self.finish:
            _ = system('clear')
            print("############################################################")
            print("######################### SNAKE ############################")
            print("############################################################")
            print("+", end="-")
            for i in range(self.width):
                print("-", end="-")
            print("+")

            for i in range(self.height):
                print("|", end=" ")
                for j in range(self.width):
                    if i == self.head[0] and j == self.head[1]:
                        print("@", end=" ")
                    elif i == self.food[0] and j == self.food[1]:
                        print("*", end=" ")
                    elif (k < len(self.print_tail)) and ((self.print_tail[k][0] == i) and (self.print_tail[k][1] == j)):
                        print("#", end=" ")
                        k = k + 1
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
            for elem in self.tail:
                if elem[0] == new_player[0] and elem[1] == new_player[1]:
                    break
            else:
                is_valid = True

        return is_valid

    def game_turn(self, in_str):
        self.lock.acquire()
        no_dir_change = False
        if ((in_str == "w" and self.direction == 0)
                or (in_str == "d" and self.direction == 1)
                or (in_str == "s" and self.direction == 2)
                or (in_str == "a" and self.direction == 3)):
            no_dir_change = True

        if not self.finish:
            if in_str == "w" and self.direction != 2:
                self.direction = 0
            elif in_str == "d" and self.direction != 3:
                self.direction = 1
            elif in_str == "s" and self.direction != 0:
                self.direction = 2
            elif in_str == "a" and self.direction != 1:
                self.direction = 3
            else:
                self.direction = self.direction

            if self.check_if_dead():
                print("Ooops, You died!")
                self.finish = True
            else:
                if no_dir_change:
                    self.move()
                    if self.check_if_food():
                        self.feed = True
                        self.generate_food()

        if self.finish:
            self.stopFlag.set()

        self.lock.release()

    def game_finish_msg(self) -> str:
        msg = "GAME OVER"
        return msg
