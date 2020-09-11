#!/usr/bin/env python3
import sys

from condep.setup import setup_pymunk_environment

from condep.parsing.cd_converter import CDConverter
from condep.parsing.SpacyParser import NLPParser, VerbLookup

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

cd_event = parser.parse_sentence(sentence)

action_events = converter.convert_cd_event_to_action_events(cd_event)

setup_pymunk_environment(action_events, sentence)
