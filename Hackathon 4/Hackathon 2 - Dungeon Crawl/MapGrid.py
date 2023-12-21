import random


class MapGrid:
    def __init__(self, width=30, height=15, walls = []):
        self.width = width
        self.height = height
        self.walls = walls
        self.player = [0, 0]
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
