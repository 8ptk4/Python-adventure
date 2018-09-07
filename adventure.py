#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Här startar spelet, med ett meny val och start som inmatning.
"""
import sys
import os
import time
import data
import cli_parser
import navigation as nav
import room_ascii

opts = cli_parser.parse_options()


if opts["args"]["info"] is True:
    print("""
    Handligen utav spelet flykten, är inte direkt vad man kan tro. Den plan jag
    hade innan jag startade koda spelet blev inte riktigt den plan jag fick senare.
    Jag tänkte från början köra 5 rum, en i mitten som sammanlänkar fyra rum i
    alla väderstreck. Efter man gjort dem fyra rummen så skulle man göra det sista
    i mitten rummet och sen klara spelet.

    Visst blev spelet tillslut ganska likt planen jag hade från början, men jag
    tycker jag kryddade till det och fick det betydligt bättre då alla rum på nått
    sätt sammanverkar med varandra, och man får se hur mittenrummet växer fram
    och blir det slutliga rummet att klara.

    Man måste klara samtliga rum för att ha en chans att vinna, enbart då finns en
    tv och en kista med en fjärrkontroll i sista rummet att använda sig utav,
    men det går enbart att få fjärrkontrollen om man har plockat upp nyckeln från
    nyckel som man låser upp kistan i vardagsrummet med.
""")
    exit()

if opts["args"]["about"] is True:
    print("""
    Jag som gjort spelet heter Patrik Karlsson, är 33 år och bor förnuvarande
    på Aspö i Karlskrona. Läser webbprogrammering på BTH och älskar kaffe.
""")
    exit()

if opts["args"]["cheat"] is True:
    print("""
    Spelar ingen roll i vilken ordning man utför dessa.

    syd - Toaletten::
        [öppna] toalett
        [sparka] boll

    norr - Köket::
        [flytta] kärl

    öst - Kontoret::
        [sparka] lås
        [öppna] skåp
        [flytta] spak

    väst - sovrummet
        [ta] tictactoe
        [använd] tictactoe (Bra om man vinner här, jobbigt att köra om)
        [ta] nyckel (Tillkommer i rummet om man vinner tictactoe)

    vardagsrummet (mitten)
        det finns nu en tv och en kista i rummet..
        [använd] nyckel
        [ta] fjärrkontroll
        [använd] fjärrkontroll

        Eller så går det att använda cheat i vilket rum du än önskar.
""")
    exit()

# Hämtar alla rooms från rooms modulen.
rooms = data.getRooms() # rooms är ett json objekt
laddat_spel = data.loadRooms()
# Huvudfunktionen för hela spelet.
def main():
    """
    Huvudfunktion, härifrån startar allt.
    """
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X

    # Hämtar intro bild och skriver ut handligen utav spelet.
    print(room_ascii.gametitle)
    time.sleep(0.5)
    print("  Detta är flykten, med titeln att döma kanske du är fångad i ett hus och försöker")
    time.sleep(1)
    print("göra allt för att ta dig därifrån.  Eller så kanske du helt enkelt försöker sätta på")
    time.sleep(1)
    print("  en tv apparat. Du måste klara av alla rum för att ha en chans att klara spelet.")
    time.sleep(1)
    print("        Kom ihåg att använda dig utav [h, hjälp] för att se alla kommandon")
    time.sleep(1)
    print("                 En sak till förresten, du hör tydligen röster...")
    time.sleep(1)
    print("                             Lycka till MUhahaHA")
    time.sleep(1)

    time.sleep(2)
    # Spelets huvudmeny
    print("\n")
    print("                         " + "[start] " + " - Starta spelet")
    print("                         " + "[ladda] " + " - Ladda sparat spel")
    print("                         " + "[exit] " + "  - Stäng av spelet")

    while True:
        # Huvudmeny val
        val = input('\n>>>')
        if val == "start":
            nav.navigation(rooms)
        elif val == "ladda":
            nav.navigation(laddat_spel)
        elif val == "exit":
            sys.exit()
        else:
            print("Finns inget val för", val)

if __name__ == "__main__":
    main()
