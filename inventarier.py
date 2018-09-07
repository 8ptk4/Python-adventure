#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modul som hanterar spelarens inventarier.
"""
import os
import sys
import time
import tictactoe as ttt
import room_ascii


def inventarier_ta(sak, room, inventarier):
    """
    Hanterar om spelaren plockar upp objekt.
    """
    # Om man försöker ta tictactoe, nyckel eller fjärrkontroll.
    if sak == "tictactoe" or sak == "nyckel" or sak == "fjärrkontroll":
        inventarier.append(sak)
        room['objekt'].remove(sak)
        print("En röst säger>> Du plockade upp", sak, "från rummet till dina inventarier!.")
    # Om man försöker plocka upp något annat objekt än tictactoe, nyckel eller
    # fjärrkontroll.
    elif sak != "tictactoe" or sak != "nyckel" or sak != "fjärrkontroll":
        print("En röst säger>> Du kan inte ta upp objektet", sak)

def inventarier_drop(sak, room, inventarier):
    """
    Hanterar om spelaren släpper objekt.
    """
    # Om man försöker släppa tictactoe, nyckel eller fjärrkontroll vilka
    # är spelets alla möjliga objekt att kunna ta.
    if sak == "tictactoe" or sak == "nyckel" or sak == "fjärrkontroll":
        inventarier.remove(sak)
        room['objekt'].append(sak)
        print("En röst säger>> Du släppte objektet", sak, "från dina inventarier till rummet!.")
    # Om inte tictactoe, nyckel eller fjärrkontroll finns i spelarens inventarier.
    elif sak != "tictactoe" or sak != "nyckel" or sak != "fjärrkontroll":
        print("En röst säger>> Objektet ", sak, "finns inte i dina inventarier!.")


def inventarier_use(sak, room, inventarier, rooms):
    """
    Hanterar om spelaren försöker använda objekt från sitt inventarie.
    """
    # Om man använder tictactoe och tictactoe finns i inventarierna.
    if sak == "tictactoe":
        if sak in inventarier:
            ttt.tictactoe(rooms, inventarier)

    # Om man använder nyckel och den finns i inventarierna.
    if sak == "nyckel" and sak in inventarier:
        if room['name'] == "vardagsrummet":
            if "kista" in room['objekt']:
                room['kista_öppnad'] = 1
                print("En röst säger>> Du använder nyckeln och låser upp kistan på golvet!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("En röst säger>> I kistan ligger en fjärrkontroll till tv:n.")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print(">> Fjärrkontroll finns nu bland objekten i rummet!.")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                room['objekt'].append("fjärrkontroll")
                inventarier.remove("nyckel")
            else:
                print("En röst säger>> Du har inget objekt i rummet att använda nyckeln på!")
        else:
            print("En röst säger>> Du kan inte använda nyckeln här!.")

    # Om man använder fjärrkontroll och kontoret inte är gjort. dvs ingen el i huset.
    if sak == "fjärrkontroll" and rooms['kontoret']['state'] == 0:
        print("En röst säger>> Du försöker sätta på tv:n men inget händer. Kanske har tv:n ingen ström!.")

    # Om man använder fjärrkontroll och alla rum är klara.
    if sak == "fjärrkontroll" and rooms['vardagsrummet']['state'] == 4:
        print("En röst säger>> Du trycket på fjärrkontrollen, tv:n startar!")

        # Här vinner man tydligen spelet för tillfället!.
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        rooms['vardagsrummet']['state'] = 5

        print("---------------------------------------------------------------------")
        print(room['beskrivning'][5])
        print("---------------------------------------------------------------------")

        room_ascii.get_ascii(room['ascii'][5])

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
