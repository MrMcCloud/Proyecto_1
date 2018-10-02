#!/usr/bin/env python
# -*- coding: utf-8 -*-

from definitions import avanzar_laberinto, ruta_jugador, imprimir_laberinto

final = 1
jugador = []
while final != 3:
    if final == 1:
        print("bienvenido al laberinto del minotauro")
        jugador = avanzar_laberinto()
    elif final == 2:
        print("este es el camino que recorriste ")
        imprimir_laberinto(ruta_jugador(jugador))
    print("¿que deseas hacer?\njugar de nuevo(ingrese 1)\nver el camino recorido(ingrese 2)")
    print("cerrar programa(ingrese 3)")
    final = int(input(">>>"))