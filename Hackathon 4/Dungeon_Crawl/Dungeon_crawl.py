from MapGrid import MapGrid

grid = MapGrid()
grid.get_walls()
grid.draw_grid()

while(not grid.is_finish()):
    mover = input(" w a s d")
    grid.mover_personaje(mover)
    grid.draw_grid()
print("victoria")