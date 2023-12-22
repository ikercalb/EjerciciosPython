import tiktaktoe
import Dungeon_crawl
import GameofLife


while True:
    modo = input("¿que juego quieres? TikTakToe(t), Dungeon crawl(d), GameofLife(g), para salir (s)")

    if modo == "s":
        break

    match modo:
        case "t":
            print("Juego 1: TikTakToe")
            tiktaktoe.jugar()
        case "d":
            print("Juego 2: Dungeon Crawl")
            Dungeon_crawl.jugar()
        case "g":
            print("Juego 3: Game of Life")
            GameofLife.jugar()

        case _:
            print("Juego no válido.")
