#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Här ger vi användaren val om vart man vill röra sig.
"""
import os
import commands
import room_ascii
import data
import adventure
import objekt
import inventarier as inv

# Inventarierna, objekt man kan ta sparas i denna lista.
inventarier = list()

def navigation(rooms):
    """
    Spelets ryggrad.
    """

    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X

    # Möjliga val att kunna göra
    directions = ['norr', 'syd', 'öst', 'väst']
    # Det är här vi startar
    room = rooms["vardagsrummet"]

    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X

    # skriver ut beskrivningen utav första rummet
    print("---------------------------------------------------------------------")
    print(room['beskrivning'][0])
    print("---------------------------------------------------------------------")

    room_ascii.get_ascii(room['ascii'][0])


    # While loop som hanterar valen.
    while True:

        # Input från användaren
        val = input('\n>>> ')

        # Splittrar inputen från användarna när det är dubbel kommandon.
        sak = val.split(" ")

        # Om tictactoe finns i inventarierna så kan man inte gå till andra rum!.
        if val in directions and "tictactoe" in inventarier:
            print("En röst säger>> Du MÅSTE använda tictactoe och vinna spelet, för att ta dig ut från rummet!.")

        # Om tictactoe inte finns i inventarierna kan man gå till andra rum!.
        elif val in directions and "tictactoe" not in inventarier:
            if val in room:



################################################################################
## State handler som hanterar rummens states så allt går rätt till. ############

                # När 1 av rummen är klarade(vilken ordning som helst). Och vardagsrummet state är 0.
                # Sätter vardagsrummet till state 1.

                if rooms['vardagsrummet']['state'] == 0:
                    if rooms['toaletten']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 1
                    if rooms['köket']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 1
                    if rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 1
                    if rooms['kontoret']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 1

                # När 2 av rummen är klarade(vilken ordning som helst). Och vardagsrummet state är 1.
                # Sätter vardagsrummet till state 2.
                if rooms['vardagsrummet']['state'] == 1:
                    if rooms['toaletten']['state'] == 1 and rooms['köket']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2
                    if rooms['toaletten']['state'] == 1 and rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2
                    if rooms['toaletten']['state'] == 1 and rooms['kontoret']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2
                    if rooms['köket']['state'] == 1 and rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2
                    if rooms['köket']['state'] == 1 and rooms['kontoret']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2
                    if rooms['kontoret']['state'] == 1 and rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 2

                # När 3 av rummen är klarade(vilken ordning som helst). Och vardagsrummet state är 2.
                # Sätter vardagsrummet till state 3. Och en tv blir tillgänglig i rummets objekt.
                if rooms['vardagsrummet']['state'] == 2:
                    if rooms['toaletten']['state'] == 1 and rooms['köket']['state'] == 1 and \
                    rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 3
                        rooms['vardagsrummet']['objekt'].append("tv")
                    if rooms['toaletten']['state'] == 1 and rooms['köket']['state'] == 1 and \
                    rooms['kontoret']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 3
                        rooms['vardagsrummet']['objekt'].append("tv")
                    if rooms['toaletten']['state'] == 1 and rooms['kontoret']['state'] == 1 and \
                    rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 3
                        rooms['vardagsrummet']['objekt'].append("tv")
                    if rooms['kontoret']['state'] == 1 and rooms['köket']['state'] == 1 and \
                    rooms['sovrummet']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 3
                        rooms['vardagsrummet']['objekt'].append("tv")

                # När alla rum är klarade och dess state är satt till 1 och vardagsrummet är state 3.
                # Sätter vardagsrummet till state 4. Och en kista blir tillgängli i rummets objekt.
                if rooms['vardagsrummet']['state'] == 3:
                    if rooms['toaletten']['state'] == 1 and rooms['köket']['state'] == 1 and \
                    rooms['sovrummet']['state'] == 1 and rooms['kontoret']['state'] == 1:
                        rooms['vardagsrummet']['state'] = 4
                        rooms['vardagsrummet']['objekt'].append("kista")

################################################################################
################################################################################


                room = rooms[room[val]]

                commands.room_description(room)

                # Dessa är testing......................
                #print(rooms['vardagsrummet']['state'])
                # print(rooms['sovrummet']['state'])
                # print(inventarier)

                # Skriver ut ascii bilden kopplad till rummet detta gör så att
                # vardagsrummet blir korrekt eftersom rummet har fler än två states.
                if room['state'] == 2:
                    os.system('cls')  # For Windows
                    os.system('clear')  # For Linux/OS X
                    # skriver ut beskrivningen utav första rummet
                    print("---------------------------------------------------------------------")
                    print(room['beskrivning'][2])
                    print("---------------------------------------------------------------------")
                    room_ascii.get_ascii(room['ascii'][2])
                elif room['state'] == 3:
                    os.system('cls')  # For Windows
                    os.system('clear')  # For Linux/OS X
                    # skriver ut beskrivningen utav första rummet
                    print("---------------------------------------------------------------------")
                    print(room['beskrivning'][3])
                    print("---------------------------------------------------------------------")
                    room_ascii.get_ascii(room['ascii'][3])
                elif room['state'] == 4:
                    os.system('cls')  # For Windows
                    os.system('clear')  # For Linux/OS X
                    # skriver ut beskrivningen utav första rummet
                    print("---------------------------------------------------------------------")
                    print(room['beskrivning'][4])
                    print("---------------------------------------------------------------------")
                    room_ascii.get_ascii(room['ascii'][4])
            else:
                print("Du kan inte gå dit.")

################################################################################
## Kommandon för spelet ########################################################

        elif val in ("i", "info"):
            commands.room_description(room)
        elif val in ("l", "ledtråd"):
            commands.room_hint(room)
        elif val in ("o", "objekt"):
            commands.room_objects(room)
        elif val in ("h", "hjälp"):
            commands.room_help()
        elif val == "se":
            commands.room_see(room)
        elif val in ("c", "cheat"):
            commands.room_cheat(room, inventarier, rooms)

################################################################################
## Kommandon för inventarier ###################################################

        elif val in ("inv, inventarier"):
            inventarier_num = len(inventarier)
            if inventarier_num == 0:
                print("Du har inga objekt i dina inventarier!.")
            elif inventarier_num == 1:
                print("Du har 1 objekt i dina inventarier:")
                print(inventarier)
            elif inventarier_num == 2:
                print("Du har 2 objekt i dina inventarier:")
                print(inventarier)

        # Kollar om man har skrivit två ord i prompten
        # Valet i prompten är sen splitat och orden jämförs nedan
        elif len(sak) == 2:

################################################################################
## Dessa är kommandon för vad man kan göra med ett objekt ######################

            if sak[0] in ("titta", "t"):
                if sak[1] in room['objekt']:
                    objekt.objekt_titta(sak[1], room)
                else:
                    print("En röst säger>> Finns inget objekt att titta närmare på vid namn", sak[1])

            elif sak[0] in ("öppna", "ö"):
                if sak[1] in room['objekt']:
                    objekt.object_open(sak[1], room)
                else:
                    print("En röst säger>> Finns ingeet objekt att öppna vid namn", sak[1])

            elif sak[0] in ("sparka", "s"):
                if sak[1] in room['objekt']:
                    objekt.object_kick(sak[1], room, rooms)
                else:
                    print("En röst säger>> Finns inget objekt att sparka på i rummet som matchar", sak[1])

            elif sak[0] in ("flytta", "f"):
                if sak[1] in room['objekt']:
                    objekt.object_move(sak[1], room, rooms)
                else:
                    print("En röst säger>> Finns inget objekt i rummet att flytta vid namn", sak[1])

################################################################################
## Dessa är kommandon för vad man kan göra med inventarier #####################

            elif sak[0] == "ta":
                if sak[1] in room['objekt']:
                    inv.inventarier_ta(sak[1], room, inventarier)
                else:
                    print("En röst säger>> Finns inget objekt i rummet att ta vid namn", sak[1])

            elif sak[0] in ("släpp", "sl"):
                if sak[1] in inventarier:
                    inv.inventarier_drop(sak[1], room, inventarier)
                else:
                    print("En röst säger>> Finns inget objekt att släppa från dina inventarier vid namn", sak[1])

            elif sak[0] in ("använd", "a"):
                if sak[1] in inventarier:
                    inv.inventarier_use(sak[1], room, inventarier, rooms)
                else:
                    print("En röst säger>> Finns inget objekt att använda vi namn", sak[1])
            else:
                print("En röst säger>> Nått som inte stämmer, testa igen!.")

        # Om val är spara sparar json objektet till fil. Vilket man sen kan ladda
        # från huvudmenyn
        elif val == "spara":
            data.saveRooms(rooms)
            adventure.main()

        # Avslutar spelet och återgår till huvudmenyn
        elif val == "sluta":
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            adventure.main()

        else:
            print("Förstår inte vad du menar.")
