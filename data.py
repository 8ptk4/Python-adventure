#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hämtar data från fil i formatet json och gör om till ett json objekt
"""
import json

# Detta är filen med alla rum, states osv.
rooms_file = "rooms.json"
# Den sparade filen...
saved_file = "save.json"


# Hämtar rummen från fil och gör till ett json objekt
def getRooms():
    """
    Funktion som tar in json fil och konverterar till json objekt.
    """
    json_file = open(rooms_file, "r")
    rooms = json.load(json_file)
    json_file.close()
    return rooms

def saveRooms(rooms):
    """
    Sparar json data i fil.
    """
    with open('save.json', 'w') as outfile:
        json.dump(rooms, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    print("Game saved!")

def loadRooms():
    """
    Laddar sparat spel.
    """
    json_file = open(saved_file, "r")
    rooms = json.load(json_file)
    json_file.close()
    return rooms
