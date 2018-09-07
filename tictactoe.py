#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tictactoe spelet, med funktioner som sköter allt från att skapa matrisen
till att hantera användarens inmatning samt randomiserar datorns
"""
from random import randint
import time
import os
import room_ascii


def createMatrix(y, x, filler):
    """
    Create a two-dimensional array and return it.
    """
    return [[filler for _ in range(x)] for _ in range(y)]

def printMatrix(matrix):
    """
    Print the content of the matrix.
    """
    for row in matrix:
        print("     ".join(row))
        print("\n\n")

def winner(room, inventarier):
    """
    Skriver ut om man vinner tictactoe
    """

    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X


    # Efter att ha sparkat bollen
    print("---------------------------------------------------------------------")
    print(room['sovrummet']['beskrivning'][1])
    print("---------------------------------------------------------------------")
    room_ascii.get_ascii(room['sovrummet']['ascii'][1])

    print("En röst säger>> Bra jobbat! Du vann över rummet i en tic tac toe duell!")
    time.sleep(1)
    print("")
    time.sleep(1)
    print(">> Objektet nyckel tillkom nu som objekt i rummet!.")
    time.sleep(1)

    print(" ")
    if room['vardagsrummet']['state'] == 2 or room['vardagsrummet']['state'] == 3:
        print("En röst säger>> Något verkar hända i vardagsrummet!.")

    room['sovrummet']['state'] = 1


    # Lägger till objektet nyckel i rummet
    room['sovrummet']['objekt'].append("nyckel")

    # Sätter rummets state till 1 så vardagsrummets state ändras.
    room['sovrummet']['state'] = 1

    # Tar bort objektet tictactoe från inventarierna för att kunna gå ut ur rummet!.
    inventarier.remove("tictactoe")


def tictactoe(room, inventarier):
    """
    Main function to carry out the work.
    """
    y = 3
    x = 3



    matrix = createMatrix(y, x, "-")


    finished = 0
    counter = 0
    while True:
        printMatrix(matrix)

        try:
            # Swap between X and O
            if finished == 1:
                break

            if counter == 0:
                char = "X"
                posY = input("En röst säger>> Ange en rad: ")
                posX = input("En röst säger>> Ange en kolumn: ")

                posY = str((int(str(posY)) - 1))
                posX = str((int(str(posX)) - 1))




                if matrix[int(posY)][int(posX)] == char:
                    print("En röst säger>> Men ser du inte att den rutan redan är upptagen! Skärpning nu!")
                    continue
                if matrix[int(posY)][int(posX)] != char:

                    matrix[int(posY)][int(posX)] = char

                    counter += 1


                if (matrix[int(0)][int(0)] == "X" and \
                matrix[int(0)][int(1)] == "X" and \
                matrix[int(0)][int(2)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(1)][int(0)] == "X" and \
                matrix[int(1)][int(1)] == "X" and \
                matrix[int(1)][int(2)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(2)][int(0)] == "X" and \
                matrix[int(2)][int(1)] == "X" and \
                matrix[int(2)][int(2)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(0)][int(0)] == "X" and \
                matrix[int(1)][int(0)] == "X" and \
                matrix[int(2)][int(0)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(0)][int(1)] == "X" and \
                matrix[int(1)][int(1)] == "X" and \
                matrix[int(2)][int(1)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(0)][int(2)] == "X" and \
                matrix[int(1)][int(2)] == "X" and \
                matrix[int(2)][int(2)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(0)][int(2)] == "X" and \
                matrix[int(1)][int(1)] == "X" and \
                matrix[int(2)][int(0)] == "X"):
                    winner(room, inventarier)
                    break
                if (matrix[int(0)][int(0)] == "X" and \
                matrix[int(1)][int(1)] == "X" and \
                matrix[int(2)][int(2)] == "X"):
                    winner(room, inventarier)
                    break


                if any("-" in s for s in matrix):
                    print("")
                else:
                    print("En röst säger>> Vi kör om, finns ingen återvändå \
    detta måste du klar annars är du fånge här!.")
                    tictactoe(room, inventarier)
                    break




                os.system('cls')  # For Windows
                os.system('clear')  # For Linux/OS X
        except ValueError:
            print("En röst säger>> Någonting gick fel!.")

        while True:


            if counter == 1:

                char = "O"
                posY = (randint(0, 2))
                posX = (randint(0, 2))
                if matrix[int(posY)][int(posX)] == "-":

                    time.sleep(1)

                    matrix[int(posY)][int(posX)] = char
                    counter -= 1
                    # Måste göra om detta så det blir mindre rader kod. Lägga alla statemest i en if kanske..
                    if (matrix[int(0)][int(0)] == "O" and \
                    matrix[int(0)][int(1)] == "O" and \
                    matrix[int(0)][int(2)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(1)][int(0)] == "O" and \
                    matrix[int(1)][int(1)] == "O" and \
                    matrix[int(1)][int(2)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(2)][int(0)] == "O" and \
                    matrix[int(2)][int(1)] == "O" and \
                    matrix[int(2)][int(2)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(0)][int(0)] == "O" and \
                    matrix[int(1)][int(0)] == "O" and \
                    matrix[int(2)][int(0)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(0)][int(1)] == "O" and \
                    matrix[int(1)][int(1)] == "O" and \
                    matrix[int(2)][int(1)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(0)][int(2)] == "O" \
                    and matrix[int(1)][int(2)] == "O" \
                    and matrix[int(2)][int(2)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(0)][int(2)] == "O" and \
                    matrix[int(1)][int(1)] == "O" and \
                    matrix[int(2)][int(0)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break
                    if (matrix[int(0)][int(0)] == "O" and \
                    matrix[int(1)][int(1)] == "O" and \
                    matrix[int(2)][int(2)] == "O"):
                        print("En röst säger>> Du förlorade!")
                        finished += 1
                        break

            else:
                break
