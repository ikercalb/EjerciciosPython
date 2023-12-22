import configparser
import numpy as np
import sys
import random
import time

config = configparser.ConfigParser()
config.read('config.ini')




class game:

    s_width = int(config['DEFAULT']['DEFAULT_WIDTH'])
    s_height = int(config['DEFAULT']['DEFAULT_HEIGHT'])
    s_walls = []
    s_cell_num = int(config['life']['DEFAULT_CELL_INIT_ALIVE_CELL_NUM'])
    s_cell_turn = int(config['life']['DEFAULT_CELL_GAME_TURNS'])

    def __init__(self, width = s_width, height = s_height, walls = s_walls, init_alive_cell_num=s_cell_num, game_turns=s_cell_turn):
        self.width = width
        self.height = height
        self.walls = walls
        self.player = [0, 0]
        self.init_alive_cell_num = init_alive_cell_num
        self.game_turns = game_turns
        self.cells = np.zeros((self.height, self.width), dtype=bool)

    ################## Dungeon Crawl #################

    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if (j,i) in self.walls:
                    print("🧱 ", end='')
                elif i == self.player[0] and j == self.player[1]:
                    print("🧙‍♂️", end=' ')
                elif(j, i) == (self.width-1,self.height-1):
                    print("🏰", end='')
                else:
                    print(" . ", end='')
            print()

    def get_walls(self, pct= 0.03):
        self.walls = set()
        cant_paredes = round(pct * self.width * self.height)

        while len(self.walls) < cant_paredes:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.walls.add((x, y))

    def valido(self, mov):
        m= (mov[1],mov[0])
        if m not in self.walls:
            if m[0] >= 0 and m[0] < self.width and m[1] >= 0 and m[1] < self.height:
                print(m[0], m[1])
                return True
    def mover_personaje(self,mover):

        if mover == "w":
            nuevo_mov = [self.player[0] - 1, self.player[1]]
        elif mover == "a":
            nuevo_mov = [self.player[0], self.player[1] - 1]
        elif mover == "s":
            nuevo_mov = [self.player[0] + 1, self.player[1]]
        elif mover == "d":
            nuevo_mov = [self.player[0], self.player[1] + 1]
        else:
            return

        if self.valido(nuevo_mov):
            self.player = nuevo_mov
    def is_finish(self):
        if self.width-1 == self.player[1] and self.height-1 == self.player[0]:
            return True



################## Game of Life #################


    def draw_grid(self):
        s_alive = config['life']['ALIVE']
        s_dead = config['life']['DEAD']
        print("|---     |---     |        |              ")
        print("|        |--      |        |              ")
        print("|---     |---     |___     |___           ")
        for i in range(self.height):
            for j in range(self.width):

                if self.cells[i][j]:
                    print(s_alive, end='')
                    self.cells[i][j] = 1
                else:
                    print(s_dead, end='')
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


# #################tiktaktoe##################
tablero = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
jugador = 0
cont = 0


def sacar_tablero():
    print("+---+---+---+")
    print("+ " + tablero[0][0] + " + " + tablero[0][1] + " + " + tablero[0][2] + " +")
    print("+---+---+---+")
    print("+ " + tablero[1][0] + " + " + tablero[1][1] + " + " + tablero[1][2] + " +")
    print("+---+---+---+")
    print("+ " + tablero[2][0] + " + " + tablero[2][1] + " + " + tablero[2][2] + " +")
    print("+---+---+---+")
    print(cont)


def cambio_jugador():
    global jugador

    if jugador == 0:
        j = "X"
        jugador = 1
    else:
        j = "O"
        jugador = 0

    return j


def comprobar():
    # horizontales
    if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != " " and tablero[0][1] != " " and tablero[0][
        2] != " ":
        return 1, tablero[0][0]
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != " " and tablero[1][1] != " " and \
            tablero[1][2] != " ":
        return 1, tablero[1][0]
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != " " and tablero[2][1] != " " and \
            tablero[2][2] != " ":
        return 1, tablero[2][2]
    # verticales
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != " " and tablero[1][0] != " " and \
            tablero[2][0] != " ":
        return 1, tablero[0][0]
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != " " and tablero[1][1] != " " and \
            tablero[2][1] != " ":
        return 1, tablero[0][1]
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != " " and tablero[1][2] != " " and \
            tablero[2][2] != " ":
        return 1, tablero[0][2]
    # diagonales
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " " and tablero[1][1] != " " and \
            tablero[2][2] != " ":
        return 1, tablero[0][0]
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " " and tablero[1][1] != " " and \
            tablero[2][0] != " ":
        return 1, tablero[0][2]
    # empate
    elif cont == 9:
        return 2, 0
    else:
        return 0, 0


def empezar():
    global tablero
    global cont
    global jugador
    tablero = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
    jugador = 0
    cont = 0
    meter_dato()


def meter_dato():
    global cont

    while True:
        vic, jug = comprobar()
        if vic == 1:
            respuesta = input("ha ganado el juegador " + jug + " ¿Quieres jugar de nuevo? (s/n): ")
            if respuesta.lower() == 's':
                empezar()
            elif respuesta.lower() == 'n':
                sys.exit()
            else:
                print("Entrada no válida. Vuelve a intentar.")

        if vic == 2:
            respuesta = input("Empate ¿Quieres jugar de nuevo? (s/n): ")
            if respuesta.lower() == 's':
                empezar()
            elif respuesta.lower() == 'n':
                sys.exit()
            else:
                print("Entrada no válida. Vuelve a intentar.")

        pos = input("posicion de 1-9 y si quieres salir 0")

        if pos == "0":
            sys.exit()

        match pos:
            case "1":
                if tablero[2][0] == " ":
                    tablero[2][0] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "2":
                if tablero[2][1] == " ":
                    tablero[2][1] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "3":
                if tablero[2][2] == " ":
                    tablero[2][2] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "4":
                if tablero[1][0] == " ":
                    tablero[1][0] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "5":
                if tablero[1][1] == " ":
                    tablero[1][1] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "6":
                if tablero[1][2] == " ":
                    tablero[1][2] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "7":
                if tablero[0][0] == " ":
                    tablero[0][0] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "8":
                if tablero[0][1] == " ":
                    tablero[0][1] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")
            case "9":
                if tablero[0][2] == " ":
                    tablero[0][2] = cambio_jugador()
                    cont = cont + 1
                    sacar_tablero()
                else:
                    print("Prueba con otra posición")

            case _:
                print("Posicion no válida.")



