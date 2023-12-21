import sys

import numpy as np
import os

# Clearing the Screen

tablero = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
jugador = 0
cont = 0


def clear(): return os.system('clear')


def sacar_tablero():
    clear()
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
    if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != " " and tablero[0][1] != " " and tablero[0][2] != " ":
        return 1, tablero[0][0]
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != " " and tablero[1][1] != " " and tablero[1][2] != " ":
        return 1, tablero[1][0]
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != " " and tablero[2][1] != " " and tablero[2][2] != " ":
        return 1, tablero[2][2]
    # verticales
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != " " and tablero[1][0] != " " and tablero[2][0] != " ":
        return 1, tablero[0][0]
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != " " and tablero[1][1] != " " and tablero[2][1] != " ":
        return 1, tablero[0][1]
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != " " and tablero[1][2] != " " and tablero[2][2] != " ":
        return 1, tablero[0][2]
    # diagonales
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " " and tablero[1][1] != " " and tablero[2][2] != " ":
        return 1, tablero[0][0]
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " " and tablero[1][1] != " " and tablero[2][0] != " ":
        return 1, tablero[0][2]
    #empate
    elif cont==9:
        return 2,0
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
            respuesta = input("ha ganado el juegador "+ jug +" ¿Quieres jugar de nuevo? (s/n): ")
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


meter_dato()
