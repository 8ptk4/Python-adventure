#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Argparse CLI
"""
import argparse

VERSION = "Alpha - Early Access"

def _options(parser):
    group = parser.add_mutually_exclusive_group() # skapar en grupp för man vill inte kunna skicka t.ex både -v -s

    group.add_argument("-V", "--verbose", dest="verbose", default="False", help="increase output verbosity", \
    action="store_true")
    group.add_argument("-i", "--info", dest="info", default="False", help="Beskrivning av spelet och spelets idé", \
    action="store_true")
    group.add_argument("-c", "--cheat", dest="cheat", default="False", \
    help="Minsta möjliga väg för att klara spelet.", action="store_true")
    group.add_argument("-a", "--about", dest="about", default="False", \
    help="Beskrivning av dig själv, du som gjort spelet.", action="store_true")
    group.add_argument("-s", "--silent", dest="silent", default="False", help="decrease output verbosity", \
    action="store_true")
    group.add_argument("-v", "--version", action="version", version=VERSION)
    group.add_argument("-o", "--output")


    #subparser.add_parser("i", help="[filename] Get Letters")

def parse_options():
    """
    Parse all command line options and arguments and return them as a dictionary.
    """
    parser = argparse.ArgumentParser() # returnerar ett parser objekt.
    _options(parser) # kallar på funktionen add_options

    # returnerar två dictionarys i arg(alla kända saker) unknown_args(om man skickat in något utöver arg)
    arg, unknown_args = parser.parse_known_args()

    options = {}
    options["args"] = vars(arg)
    options["unknownargs"] = unknown_args

    return options
