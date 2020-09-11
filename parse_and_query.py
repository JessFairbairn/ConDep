#!/usr/bin/env python3
import sys
import tempfile

from condep.setup import setup_pymunk_environment

from condep.parsing.cd_converter import CDConverter
from condep.parsing.SpacyParser import NLPParser, VerbLookup
from condep.prolog import prolog_service

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



prolog_service.run_prolog_enivornment(cd_event)#-s prolog/condep.lgt
