#!/usr/bin/env python3
import sys
import tempfile

from pymunk_cd.setup import setup_pymunk_environment

from pymunk_cd.parsing.cd_converter import CDConverter
from pymunk_cd.parsing.NLPParser import NLPParser, VerbLookup

from pymunk_cd.prolog import converter as prolog_converter

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

tempFileWrapepr = tempfile.NamedTemporaryFile(suffix='.lgt')

predicates = prolog_converter.convert_to_prolog(cd_event)
fileContents = prolog_converter.output_logtalk_file(predicates)

with open(tempFileWrapepr.name, "w") as tempFile:
    tempFile.write(fileContents)

from subprocess import run
run(["swilgt","-s", "prolog/condep.lgt", "-s", tempFileWrapepr.name])#-s prolog/condep.lgt
