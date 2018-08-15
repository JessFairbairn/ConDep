#!/usr/bin/env python3
import sys

from pymunk_cd.setup import setup_pymunk_environment

from pymunk_cd.parsing.cd_converter import CDConverter
from pymunk_cd.parsing.NLPParser import NLPParser, VerbLookup

args = sys.argv

if len(args) == 1:
    try:
        text_file = open("input.txt", "r")
        sentence = text_file.read()
        text_file.close()
    except FileNotFoundError:
        sentence = input('Enter a sentence: ')

else:
    sentence = args[1]

verbLookup = VerbLookup()
converter = CDConverter()

parser = NLPParser(verbLookup, converter)

event = parser.parse_sentence(sentence)

action_event = converter.convert_cd_event_to_action_event(event)

setup_pymunk_environment(action_event)
