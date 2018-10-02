#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random


def numero_aleatorio():

    num = int(random()*50 + 1)
    while num < 20:
        num = int(random()*50 + 1)

    return num


def generacion_laberinto():

    num = numero_aleatorio()
    laberinto = []
    for i in range(num):
        laberinto.append(["*"]*num)

    return laberinto


def salida_laberinto():

    laberinto = generacion_laberinto()
    horizontal = int(random() * len(laberinto))
    if horizontal == 0:
        horizontal = horizontal + 1
    elif horizontal == len(laberinto) - 1:
        horizontal = horizontal - 1
    vertical = 0
    laberinto[vertical][horizontal] = "X"
    direccion_horizontal = horizontal
    direccion_vertical = vertical
    bloqueo_1 = 0
    bloqueo_2 = 0
    bloqueo_3 = 0
    bloqueo_4 = 0
    final = 1
    while final != 0:
        direccion = int(random()*4 + 1)
        magnitud = int(random()*5 + 1)
        while magnitud < 3:
            magnitud = int(random()*5 + 1)
        if direccion == 1:
            if direccion_vertical - magnitud > 0:
                i = 1
                while i < magnitud + 1:
                    direccion_vertical = direccion_vertical - 1
                    if direccion_vertical == 2:
                        laberinto[direccion_vertical][direccion_horizontal] = ' '
                        bloqueo_1 = bloqueo_1 + 1
                        i = magnitud + 1
                    elif bloqueo_1 == 0:
                        if laberinto[direccion_vertical][direccion_horizontal] == "*":
                            laberinto[direccion_vertical][direccion_horizontal] = ' '
                            i = i + 1
                            if bloqueo_3 > 0:
                                bloqueo_3 = 0
                            if bloqueo_4 > 0:
                                bloqueo_4 = 0
        elif direccion == 2:
            if direccion_vertical + magnitud < len(laberinto) - 1:
                i = 1
                while i < magnitud + 1:
                    direccion_vertical = direccion_vertical + 1
                    if direccion_vertical == len(laberinto) - 1:
                        laberinto[direccion_vertical][direccion_horizontal] = ' '
                        i = magnitud + 1
                        final = final - 1
                    elif bloqueo_2 == 0:
                        if laberinto[direccion_vertical][direccion_horizontal] == "*":
                            laberinto[direccion_vertical][direccion_horizontal] = ' '
                            i = i + 1
                            if bloqueo_3 > 0:
                                bloqueo_3 = 0
                            if bloqueo_4 > 0:
                                bloqueo_4 = 0
        elif direccion == 3:
            if direccion_horizontal - magnitud > 0:
                if direccion_vertical > 0:
                    i = 1
                    while i < magnitud + 1:
                        direccion_horizontal = direccion_horizontal - 1
                        if direccion_horizontal == 2:
                            laberinto[direccion_vertical][direccion_horizontal] = ' '
                            bloqueo_3 = bloqueo_3 + 1
                            i = magnitud + 1
                        elif bloqueo_3 == 0:
                            if laberinto[direccion_vertical][direccion_horizontal] == "*":
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_1 > 0:
                                    bloqueo_1 = 0
                                if bloqueo_2 > 0:
                                    bloqueo_2 = 0
        elif direccion == 4:
            if direccion_horizontal + magnitud < len(laberinto) - 1:
                if direccion_vertical < len(laberinto) - 1:
                    i = 1
                    while i < magnitud + 1:
                        direccion_horizontal = direccion_horizontal + 1
                        if direccion_horizontal == len(laberinto) - 2:
                            laberinto[direccion_vertical][direccion_horizontal] = ' '
                            bloqueo_4 = bloqueo_4 + 1
                            i = magnitud + 1
                        elif bloqueo_4 == 0:
                            if laberinto[direccion_vertical][direccion_horizontal] == "*":
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_1 > 0:
                                    bloqueo_1 = 0
                                if bloqueo_2 > 0:
                                    bloqueo_2 = 0

    return laberinto


def laberinto_completo():

    laberinto = salida_laberinto()
    cantidad_caminos = int(random()*20 + 1)
    while cantidad_caminos < 10:
        cantidad_caminos = int(random()*20 + 1)
    largo_camino = int(random()*10 + 1)
    while largo_camino < 5:
        largo_camino = int(random()*10 + 1)
    for i in range(cantidad_caminos):
        horizontal = int(random()*(len(laberinto)//2) + 1)
        vertical = int(random()*len(laberinto) + 1) - 1
        direccion_vertical = vertical
        direccion_horizontal = horizontal
        for j in range(largo_camino):
            direccion = int(random()*4 + 1)
            magnitud = int(random()*5 + 1)
            bloqueo_1 = 0
            bloqueo_2 = 0
            bloqueo_3 = 0
            bloqueo_4 = 0
            if direccion == 1:
                if bloqueo_1 == 0:
                    if direccion_vertical - magnitud > 0:
                        i = 1
                        while i < magnitud + 1:
                            direccion_vertical = direccion_vertical - 1
                            if direccion_horizontal > 0:
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_3 > 0:
                                    bloqueo_3 = 0
                                if bloqueo_4 > 0:
                                    bloqueo_4 = 0
                            else:
                                bloqueo_1 = bloqueo_1 + 1
                                i = magnitud + 1
            if direccion == 2:
                if bloqueo_2 == 0:
                    if direccion_vertical + magnitud < len(laberinto) - 1:
                        i = 1
                        while i < magnitud + 1:
                            direccion_vertical = direccion_vertical + 1
                            if direccion_horizontal < len(laberinto) - 1:
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_3 > 0:
                                    bloqueo_3 = 0
                                if bloqueo_4 > 0:
                                    bloqueo_4 = 0
                            else:
                                bloqueo_2 = bloqueo_2 + 1
                                i = magnitud + 1
            if direccion == 3:
                if bloqueo_3 == 0:
                    if direccion_horizontal - magnitud > 0:
                        i = 1
                        while i < magnitud + 1:
                            direccion_horizontal = direccion_horizontal - 1
                            if direccion_vertical > 0:
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_1 > 0:
                                    bloqueo_1 = 0
                                if bloqueo_2 > 0:
                                    bloqueo_2 = 0
                            else:
                                bloqueo_3 = bloqueo_3 + 1
                                i = magnitud + 1
            if direccion == 4:
                if bloqueo_4 == 0:
                    if direccion_horizontal + magnitud < len(laberinto) - 1:
                        i = 1
                        while i < magnitud + 1:
                            direccion_horizontal = direccion_horizontal + 1
                            if direccion_vertical < len(laberinto) - 1:
                                laberinto[direccion_vertical][direccion_horizontal] = ' '
                                i = i + 1
                                if bloqueo_1 > 0:
                                    bloqueo_1 = 0
                                if bloqueo_2 > 0:
                                    bloqueo_2 = 0
                            else:
                                bloqueo_4 = bloqueo_4 + 1
                                i = magnitud + 1
    return laberinto


def ruta_jugador(data):

    for i in range(len(data[0])):
        for j in range(len(data[0][i])):
            for k in range(len(data[1])):
                if data[0][i][j] != "*":
                    if i == data[1][k] and j == data[2][k]:
                        data[0][i][j] = "X"
    return data[0]


def avanzar_laberinto():

    laberinto = laberinto_completo()
    jugador_vertical = 0
    jugador_horizontal = 0
    posiciones_verticales = []
    posiciones_horizontales = []
    almacenamiento_data = []
    final = 1
    for i in range(len(laberinto)):
        if laberinto[0][i] == "X":
            jugador_horizontal = i
    print("para salir del laberinto utilice las teclas: w(arriba), s(abajo), a(izquierda) y d(derecha) para moverse")
    while final != 0:
        imprimir_laberinto(laberinto)
        movimiento = str(input(">>>"))
        while movimiento != "w" and movimiento != "s" and movimiento != "a" and movimiento != "d":
            print("la tecla ingresada es un numero, una letra en mayuscula o una letra distinta de: w, s, a, d.")
            movimiento = str(input("ingrese otra tecla \n>>>"))
        if movimiento == "w":
            if jugador_vertical > 0:
                jugador_vertical = jugador_vertical - 1
                if laberinto[jugador_vertical][jugador_horizontal] != "*":
                    laberinto[jugador_vertical][jugador_horizontal] = "X"
                    laberinto[jugador_vertical + 1][jugador_horizontal] = ' '
                    posiciones_verticales.append(jugador_vertical)
                    posiciones_horizontales.append(jugador_horizontal)
                else:
                    print("no se puede mover en esa direccion ya que hay una pared ")
                    jugador_vertical = jugador_vertical + 1
        elif movimiento == "s":
            if jugador_vertical < len(laberinto):
                jugador_vertical = jugador_vertical + 1
                if jugador_vertical == len(laberinto):
                    laberinto[jugador_vertical - 1][jugador_horizontal] = ' '
                    final = final - 1
                    print("¡¡¡¡felicidades has salido del laberinto!!!!")
                elif laberinto[jugador_vertical][jugador_horizontal] != "*":
                    laberinto[jugador_vertical][jugador_horizontal] = "X"
                    laberinto[jugador_vertical - 1][jugador_horizontal] = ' '
                    posiciones_verticales.append(jugador_vertical)
                    posiciones_horizontales.append(jugador_horizontal)
                else:
                    print("no se puede mover en esa direccion ya que hay una pared.")
                    jugador_vertical = jugador_vertical - 1
        elif movimiento == "a":
            if jugador_horizontal > 0:
                jugador_horizontal = jugador_horizontal - 1
                if laberinto[jugador_vertical][jugador_horizontal] != "*":
                    laberinto[jugador_vertical][jugador_horizontal] = "X"
                    laberinto[jugador_vertical][jugador_horizontal + 1] = ' '
                    posiciones_verticales.append(jugador_vertical)
                    posiciones_horizontales.append(jugador_horizontal)
                else:
                    print("no se puede mover en esa direccion ya que hay una pared.")
                    jugador_horizontal = jugador_horizontal + 1
        elif movimiento == "d":
            if jugador_horizontal < len(laberinto):
                jugador_horizontal = jugador_horizontal + 1
                if laberinto[jugador_vertical][jugador_horizontal] != "*":
                    laberinto[jugador_vertical][jugador_horizontal] = "X"
                    laberinto[jugador_vertical][jugador_horizontal - 1] = ' '
                    posiciones_verticales.append(jugador_vertical)
                    posiciones_horizontales.append(jugador_horizontal)
                else:
                    print("no se puede mover en esa direccion ya que hay una pared.")
                    jugador_horizontal = jugador_horizontal - 1
        almacenamiento_data.append(laberinto)
        almacenamiento_data.append(posiciones_verticales)
        almacenamiento_data.append(posiciones_horizontales)
    return almacenamiento_data


def imprimir_laberinto(laberinto):

    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            print(laberinto[i][j], end=' ')
        print("")
    print("")


########################################################################
