#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul med funktioner som hanterar spelets funktioner.
"""
import os
import time
import sys
import room_ascii


def room_hint(room):
    """
    Kollar ledtrådarna för rummen.
    """
    if room['state'] == 0:
        print(room['ledtråd'][0])
        room['ledtråd'] += [room['ledtråd'].pop(0)]
    elif room['state'] == 1:
        print("En röst säger>> Finns inga ledtrådar längre.")
    elif room['state'] == 3:
        print(room['ledtråd_3'][0])
        room['ledtråd_3'] += [room['ledtråd_3'].pop(0)]
    elif room['state'] == 4:
        print(room['ledtråd_4'][0])
        room['ledtråd_4'] += [room['ledtråd_4'].pop(0)]


def room_description(room):
    """
    Skriver ut beskrivnigarna utav rummen.
    """
    if room['state'] == 0:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        # skriver ut beskrivningen utav första rummet
        print("---------------------------------------------------------------------")
        print(room['beskrivning'][0])
        print("---------------------------------------------------------------------")
        room_ascii.get_ascii(room['ascii'][0])

    elif room['state'] == 1:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        # skriver ut beskrivningen utav första rummet
        print("---------------------------------------------------------------------")
        print(room['beskrivning'][1])
        print("---------------------------------------------------------------------")
        room_ascii.get_ascii(room['ascii'][1])


def room_objects(room):
    """
    Visa objekten för varje rum.
    """
    objekt_antal = len(room['objekt'])

    if objekt_antal > 0:
        print("En röst säger>> Det finns " + str(len(room['objekt'])) + " objekt i rummet!.")
        print(room['objekt'])
    else:
        print("En röst säger>> Det finns inga objekt i rummet!.")


def room_help():
    """
    Skriver ut hjälp texten för alla kommandon i spelet.
    """
    print("""
    ::Kommandon::

    [i, info]    - Skriver ut beskriving utav rummet, samma som visas när man kommer in i rummet.
    [h, hjälp]   - Skriver ut en lista av de kommandon som du kan göra.
    [se]         - Titta dig runt omkring - Spelet svarar med om det finns något särskilt att se i rummet.
    [l, ledtråd] - Ge en ledtråd, eller fler om det finns, en ledtråd för varje gång man skriver kommandot.
    [c, cheat]   - Utför automatiskt alla handlingar i som krävs för att klara rummet användaren står i.

    ::Kommandon - Objekt::

    [o, objekt]           - Skriver ut vilka objekt som finns i rummet.
    [t, titta]  [objekt]  - Skriver ut beskrivningen av objektet.
    [ö, öppna]  [objekt]  - Öppna objekt om det går att öppna.
    [s, sparka] [objekt]  - Sparka på objekt så det går sönder, om det kan gå sönder.
    [f, flytta] [objekt]  - Flytta på objektet så det hamnar på en annan plats, om det går att flytta.

    ::Kommandon - Inventarie::

    [inv, inventarier]    - Skriver ut vilka objekt som finns i inventarierna.
    [ta]        [objekt]  - Ta ett objekt, om det går, och lägg i inventarierna.
    [sl, släpp] [objekt]  - Släpp ett objekt som ligger i dina inventarier.
    [a, använd] [objekt]  - Använd ett objekt.
    """)


def room_see(room):
    """
    Skriver ut vad som går att se i rummen.
    """
    if room['state'] == 0:
        print(room['se'][0])
    if room['state'] == 1:
        print(room['se'][1])


def room_cheat(room, inventarier, rooms):
    """
    Gör allt som skall göras i det aktiva rummet.
    """
#####################################################################################
## Cheat för rummet Toaletten #######################################################

    if room['name'] == "toaletten":
        if room['state'] == 0:
            room['toalett_öppnad'] = 1
            room['state'] = 1
            room['cheat'] = 1

            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(">> Cheat aktiverat.")
            time.sleep(2)
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            time.sleep(1)

            # skriver ut beskrivningen utav första rummet
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])

            print("En röst säger>> Rummet avklarat finns inget mer att göra här!.")
            #if room['vardagsrummet']['state'] == 2:
                #print("Du hör bullrande ifrån vardagsrummet")
        else:
            print("En röst säger>> Du kan inte fuska på ett rum du redan klarat!.")

######################################################################################
## Cheat för rummet Köket ############################################################

    if room['name'] == "köket":
        if room['state'] == 0:
            room['kärl_flyttad'] = 1
            room['brasa_aktiv'] = 0
            room['state'] = 1


            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(">> Cheat aktiverat.")
            time.sleep(2)
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            time.sleep(1)

            # skriver ut beskrivningen utav första rummet
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])
            print("En röst säger>> Rummet avklarat finns inget mer att göra här!.")
        else:
            print("En röst säger>> Du kan inte fuska på ett rum du redan klarat!.")


######################################################################################
## Cheat för tictactoe ###############################################################

    if room['name'] == "sovrummet":
        if room['state'] == 0:
            room['state'] = 1


            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(">> Cheat aktiverat.")
            time.sleep(2)
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            time.sleep(1)

            # skriver ut beskrivningen utav första rummet
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])

            print("En röst säger>> Rummet avklarat finns inget mer att göra här!.")
            time.sleep(1)
            print("")
            time.sleep(1)
            inventarier.append("nyckel")
            print(">> Nyckel finns nu i inventariet!.")
            room['objekt'].remove("tictactoe")

        else:
            print("En röst säger>> Du kan inte fuska på ett rum du redan klarat!.")

######################################################################################
## Cheat för kontoret ################################################################

    if room['name'] == "kontoret":
        if room['state'] == 0:
            room['state'] = 1
            room['lås_öppnad'] = 1
            room['skåp_öppnad'] = 1
            room['spak_on'] = 1


            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(">> Cheat aktiverat.")
            time.sleep(2)
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            time.sleep(1)

            # skriver ut beskrivningen utav första rummet
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])
            print("En röst säger>> Rummet avklarat finns inget mer att göra här!.")

        else:
            print("En röst säger>> Du kan inte fuska på ett rum du redan klarat!.")

######################################################################################
## Cheat för kontoret ################################################################

    if room['name'] == "vardagsrummet":
        if room['state'] == 0 or room['state'] != 0:
            rooms['toaletten']['state'] = 1
            rooms['kontoret']['state'] = 1
            rooms['sovrummet']['state'] = 1
            rooms['köket']['state'] = 1
            rooms['sovrummet']['objekt'].remove("tictactoe")
            room['state'] = 5
            room['lås_öppnad'] = 1
            room['skåp_öppnad'] = 1
            room['spak_on'] = 1

            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(">> Cheat aktiverat.")
            time.sleep(2)
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            time.sleep(1)

            # skriver ut beskrivningen utav sista rummet
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][5])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][5])
            print("En röst säger>> Rummet avklarat finns inget mer att göra här!.")

            time.sleep(5)

            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print(" ")
            print(" ")
            print(" ")
            time.sleep(0.5)
            print(r"        ,--. .   .    |   |,---.,---.    ,---.,---.,---.|    ,---.--.--")
            time.sleep(0.5)
            print(r"        |   ||   |    |---||---||---'    `---.|---'|--- |    |---|  |  ")
            time.sleep(0.5)
            print(r"        |   ||   |    |   ||   ||  \         ||    |    |    |   |  |  ")
            time.sleep(0.5)
            print(r"        `--' `---'    `   '`   '`   `    `---'`    `---'`---'`   '  `  ")
            print(room_ascii.gametitle)
            time.sleep(1)
            print("                          Ett spel av Patrik Karlsson")
            time.sleep(5)
            sys.exit()

        else:
            print("En röst säger>> Du kan inte fuska på ett rum du redan klarat!.")
