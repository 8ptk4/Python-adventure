#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hanterar objekten här
"""
import os
import time
import room_ascii


def object_options(objekt, val):
    """
    Hanterar objekten i spelet
    """
    print(objekt)
    print(val)

def print_room_objects(objekt):
    """
    Skriver ut dem olika objekten i rummet
    """

    print(objekt)

def handle_object(objekt, val):
    """
    Vet inte vad detta är måste kolla!
    """
    print("hmm här kör vi och kollar lite")
    print(objekt)
    print(val)

#######################################################################################
#######################################################################################

def objekt_titta(sak, room):
    """
    Hanterar objekt i rummen om dem går att titta, eller inte titta på.
    """
#######################################################################################
## Hanterar objekt i rummet Toaletten #################################################

    if sak == "toalett" and room['toalett_öppnad'] == 0:
        #Skriver ut beskrivningen utav toaletten!
        print(room['toalett_beskrivning'])

    if sak == "toalett" and room["toalett_öppnad"] == 1:
        print("En röst säger>> En vit toalett, med locket uppfälld!.")

    elif sak == "boll":
        #Skriver ut beskrivningen utav bollen!
        print(room['objekt_boll'])


#######################################################################################
## Hanterar objekt i rummet Köket #####################################################

    if sak == "kärl" and room['kärl_flyttad'] == 0:
        print(room['kärl_beskrivning'])

    if sak == "kärl" and room['kärl_flyttad'] == 1:
        print("En röst säger>> Kärlet är nu tomt, finns inget vatten kvar!.")

    if sak == "brasa" and room['brasa_aktiv'] == 1:
        print("En röst säger>> Brasan brinner intensivt, kan nästan inte vara nära den!.")

    if sak == "brasa" and room['brasa_aktiv'] == 0:
        print("En röst säger>> Allt som återstår är en hög av aska, finns inget annat av intresse!.")

######################################################################################
## Hanterar objekt i Sovrummet #######################################################

    if sak == "tictactoe":
        print("En röst säger>> Detta objekt kan du ta till ditt inventarie, och använda men var försiktig \
du kan bli fast i rummet förevigt!.")

    if sak == "nyckel":
        print("En röst säger>> Detta objekt kan du ta, samt använda på något lämpligt föremål.")

######################################################################################
## Hanterar objekt i vardagsrummet ###################################################

    if sak == "fjärrkontroll":
        print("En röst säger>> Detta objekt verkar ha en funktion, kanske är det att slå på tv:n, men\
du måste ta den först.")

    if sak == "tv":
        print("En röst säger>> En tv av märket ssnugma, finns inga knappar, antar den styrs med en fjärrkontroll!.")

    if sak == "kista" and room['kista_öppnad'] == 0:
        print("En röst säger>> En gammal kista, tror det behövs en nycket för att öppna!.")

    if sak == "kista" and room['kista_öppnad'] == 1:
        print("En röst säger>> Kistan är öppnad antar du har tagit fjärrkontrollen redan!.")

######################################################################################
## Hanterar objekt på kontoret #######################################################

    if sak == "lås":
        print("En röst säger>> Låset är rostigt, man kan nog ha sönder det med våld.")

    if sak == "skåp":
        print("En röst säger>> Ett gammalt proppskåp men är helt brukligt!.")

    if sak == "spak":
        print("En röst säger>> En spak av någon slags metall, funkar nog fortfarande.")




def object_open(sak, room):
    """
    Hanterar objekt i rummen om dem går att öppna, inte öppna eller om dem
    är öppnade redan.
    """
#######################################################################################
## Hanterar objket i rummet Toaletten #################################################

    if sak == "toalett" and room['toalett_öppnad'] == 0:
        # Skriver ut om toaletten är öppnad eller ej, för sak
        print("En röst säger>> Locket på toaletten är nu uppfälld!.")
        room['toalett_öppnad'] = 1
        # Skriver ut om toaletten är öppnad eller ej mest för sak
        #print(room['toalett_öppnad'])
    elif sak == "toalett" and room['toalett_öppnad'] == 1:
        print("En röst säger>> Du har redan öppnat toaletten!.")

    if sak == "boll":
        print("En röst säger>> Det går så klart inte att öppna en boll, så stronk är du inte än!.")

#######################################################################################
## Hanterar objekt i rummet Köket #####################################################

    if sak == "kärl":
        print("En röst säger>> Du kan inte öppna kärlet då det redan är öppnad!.")

    if sak == "brasa":
        print("En röst säger>> Vet inte varför du skulle vilja öppna brasan!.")

######################################################################################
## Hanterar objekt i rummet Sovrummet ################################################

    if sak == "tictactoe" or sak == "nyckel":
        print("En röst säger>> Går inte att öppna objektet!.")

######################################################################################
## Hanterar objekt i vardagsrummet ###################################################

    if sak == "kista":
        print("En röst säger>> Du kan inte öppna objektet, tror du behöver använda dig utav en nyckel")

    if sak == "fjärrkontroll" or sak == "tv":
        print("En röst säger>> Du kan inte öppna objektet!.")

######################################################################################
## Hanterar objekt på kontoret #######################################################
    if sak == "lås":
        print("En röst säger>> Kan inte öppna låset för hand!.")

    if sak == "spak":
        print("En röst säger>> Du kan inte öppna en spak!.")

    if sak == "skåp" and room['lås_öppnad'] == 1:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        # Efter att ha öppnat proppskåpet
        print("---------------------------------------------------------------------")
        print(room['beskrivning'][3])
        print("---------------------------------------------------------------------")
        room_ascii.get_ascii(room['ascii'][3])

        room['skåp_öppnad'] = 1
        print("En röst säger>> Du öppnar proppskåpet.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("En röst säger>> I skåpet sitter det en spak som pekar mot off.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        room['objekt'].append("spak")
        print(">> Objektet spak tillkom i rummet!.")


    elif sak == "skåp" and room['lås_öppnad'] == 0:
        print("En röst säger>> Du måste få upp låset på nått sätt!.")






def object_kick(sak, room, rooms):
    """
    Här hanterar vi objekt om det går att sparka eller inte.
    """

#########################################################################################
## Hanterar objekt på toaletten #########################################################

    if sak == "toalett" and room['toalett_sparkad'] == 0:
        print("En röst säger>> Du kan inte sparka på toaletten!. Gör ju skit ont i foten!.")
    elif sak == "boll" and room['boll_sparkad'] == 1:
        if room['toalett_öppnad'] == 0:
            print("En röst säger>> Du sparkar bollen och den flyger runt i rummet, men stannar snart snart igen!.")
        elif sak == "boll" and room['state'] == 1:
            print("En röst säger>> Du kan inte sparka på bollen, den sitter fast som berget i toaletten")
        elif room['toalett_öppnad'] == 1:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X

            # Efter att ha sparkat bollen
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])

            print("En röst säger>> Du gjorde det, du sparkade bollen rätt ner i toaletten.")
            time.sleep(1)
            print("")
            time.sleep(1)
            print("En röst säger>> Finns inte mer att göra här nu!.")
            time.sleep(1)
            print(" ")
            if rooms['vardagsrummet']['state'] == 2 or rooms['vardagsrummet']['state'] == 3:
                print("En röst säger>> Något verkar hända i vardagsrummet!.")
            time.sleep(1)
            room['state'] = 1

#########################################################################################
## Hanterar objekt på kontoret ##########################################################

    elif sak == "lås" and room['lås_öppnad'] == 0:
        room['lås_öppnad'] = 1
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        # Efter att ha sparkat låset
        print("---------------------------------------------------------------------")
        print(room['beskrivning'][2])
        print("---------------------------------------------------------------------")
        room_ascii.get_ascii(room['ascii'][2])

        print("En röst säger>> Värsta ninjasparken, det funka!. Låset är borta.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(">> Objektet", sak, "finns inte längre i rummet!.")
        room['objekt'].remove("lås")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("En röst säger>> Nu återstår endast proppskåpet!.")

    else:
        print("En röst säger>> Det går inte att sparka på det!")




def object_move(sak, room, rooms):
    """
    Hanterar objekt om dem går att flytta eller inte.
    """
################################################################################
## Hantera objekt i rummet Köket ###############################################

    if sak == "kärl" and room['kärl_flyttad'] == 1:
        print("En röst säger>> Kärlet står bra där den står!.")

    if sak == "kärl" and room['kärl_flyttad'] == 0:
        room['kärl_flyttad'] = 1
        room['brasa_aktiv'] = 0
        room['state'] = 1

        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        # Efter att ha sparkat låset
        print("---------------------------------------------------------------------")
        print(room['beskrivning'][1])
        print("---------------------------------------------------------------------")
        room_ascii.get_ascii(room['ascii'][1])

        print("En röst säger>> Du flyttar kärlet med vatten till brasan och häller ut allt vatten så brasan slocknar!.")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("En röst säger>> Bra jobbat, nu räddade vi huset från att brinna ner till grunden!.")
        time.sleep(1)
        print(" ")
        if rooms['vardagsrummet']['state'] == 2 or rooms['vardagsrummet']['state'] == 3:
            time.sleep(1)
            print("En röst säger>> Något verkar hända i vardagsrummet!.")


    if sak == "brasa":
        print("En röst säger>> Det går inte att flytta på brasan!.")

################################################################################
## Hantera objekt i rummet Vardagsrummet #######################################

    if sak == "tv" or sak == "kista":
        print("En röst säger>> Det går inte att flytta på objektet.", sak)

################################################################################
## Hantera objekt i rummet Toaletten ###########################################

    if sak == "toalett":
        print("En röst säger>> Du kan inte flytta på toaletten, den sitter fast alldeles för hårt!.")

    if sak == "boll":
        print("En röst säger>> Du kan inte flytta på bollen, dina armar räcker inte till!.")

################################################################################
## Hantera objekt i rummet Sovrummet ###########################################

    if sak == "tictactoe":
        print("En röst säger>> Du kan inte flytta på objektet!.")

################################################################################
## Hantera objekt på kontoret ##################################################

    if sak == "spak":
        if room['lås_öppnad'] == 1 and room['skåp_öppnad'] == 1 and room['spak_on'] == 0:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X

            # Efter att ha sparkat låset
            print("---------------------------------------------------------------------")
            print(room['beskrivning'][1])
            print("---------------------------------------------------------------------")
            room_ascii.get_ascii(room['ascii'][1])

            print("En röst säger>> Du drar i spaken!.")
            room['spak_on'] = 1
            time.sleep(1)
            print(" ")
            print("En röst säger>> Lampan ovanför ditt huvud tändes!.")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("En röst säger>> Verkar som vi fick igång elen i huset!.")
            time.sleep(1)
            print(" ")
            if rooms['vardagsrummet']['state'] == 2 or rooms['vardagsrummet']['state'] == 3:
                time.sleep(1)
                print("En röst säger>> Något verkar hända i vardagsrummet!.")


                room['state'] = 1

        elif sak == "spak" and room['spak_on'] == 1:
            print("En röst säger>> Du har redan flyttat på objektet.")

    #else:
        #print("En röst säger>> Du har redan flyttat på objektet.")

    if sak == "lås" or sak == "låda" or sak == "skåp":
        print("En röst säger>> Du kan inte flytta på objektet", sak)



        #commands.room_description(room, rooms)
