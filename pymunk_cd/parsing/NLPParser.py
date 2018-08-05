import sys

from pymunk_cd.parsing.cd_converter import CDConverter
from .VerbSense import VerbArgument, VerbSense

class VerbLookup:
    
    def get_verb(self, verb):
        #TODO: add PropBank or something      
        arg0 = VerbArgument('mock agent for verb', 'PAG')
        arg1 = VerbArgument('mock patient for verb', 'PPT')
        return VerbSense(verb, [arg0, arg1])
        
        

class NLPParser:
    def __init__(self, verbLookup:VerbLookup, cdConverter:CDConverter):
        self.verbLookup = verbLookup
        self.cdConverter = cdConverter

    def parse_sentence(self, sentence:str):
        '''Takes a sentence, does NLP stuff to get a verb event, and then
        calls the converter to turn it into a CD event'''
        words = sentence.split()

        verb = words[1]
        if verb.endswith('s'):
            verb = verb[:-1]
        
        verb_info = self.verbLookup.get_verb(verb)
        
        verb_info.get_verb_subject().argument = words[0]

        if len(words) == 3:
            verb_info.get_verb_object().argument = words[2]
        elif len(words) > 3:
            raise NotImplementedError('Can\'t handle sentences longer than 3 words yet sorry...')

        return self.cdConverter.convert_verb_event_to_cd_event(verb_info)
        