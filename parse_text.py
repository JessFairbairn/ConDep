import sys

from pymunk_cd.parsing.cd_converter import CDConverter
from pymunk_cd.parsing.NLPParser import NLPParser, VerbLookup

args = sys.argv

if len(args) == 1:
    print('Enter a sentence')
    exit()

verbLookup = VerbLookup()
converter = CDConverter()

parser = NLPParser(verbLookup, converter)

event = parser.parse_sentence(args[1])