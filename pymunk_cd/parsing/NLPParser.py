import sys

from pymunk_cd.parsing.cd_converter import CDConverter
from .VerbSense import *

class VerbLookup:
    
    def get_verb(self, verb):
        if verb == "emit":
            arg0 = VerbArgument('emitting entity', 'PAG')
            arg1 = VerbArgument('thing emitted', 'PPT')
            return VerbSense("emit", [arg0, arg1])
        else:
            # TODO: Actually look it up...
            raise NotImplementedError
        

class NLPParser:
    def __init__(self, verbLookup:VerbLookup, cdConverter:CDConverter):
        self.verbLookup = verbLookup
        self.cdConverter = cdConverter

    def parse_sentence(self, sentence:str):
        '''Takes a sentence, does NLP stuff to get a verb event, and then
        calls the converter to turn it into a CD event'''
        words = sentence.split()
        if " emit" in sentence:
            verb_info = self.verbLookup.get_verb('emit')
            
            verb_info.get_verb_subject().argument = words[0]
            verb_info.get_verb_object().argument = words[2]

            return self.cdConverter.convert_verb_event_to_cd_event(verb_info)
        else:
            raise NotImplementedError