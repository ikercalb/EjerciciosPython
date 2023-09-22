#!/usr/bin/env python3
palabra = input("escribe una palabra")
palabra_alreves = palabra[::-1]
if palabra == palabra_alreves:
    print("la palabra "+palabra+" es palindromo")
else:
    print("no es palindromo")