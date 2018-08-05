import sys

from pymunk_cd.utilities import stringify_entity

from pymunk_cd.setup import setup_pymunk_environment

from pymunk_cd.parsing.cd_converter import CDConverter
from pymunk_cd.parsing.NLPParser import NLPParser, VerbLookup

args = sys.argv

if len(args) == 1:
    sentence = input('Enter a sentence: ')
else:
    sentence = args[1]

verbLookup = VerbLookup()
converter = CDConverter()

parser = NLPParser(verbLookup, converter)

event = parser.parse_sentence(sentence)


print(event)

action_event = converter.convert_cd_event_to_action_event(event)

setup_pymunk_environment(action_event)