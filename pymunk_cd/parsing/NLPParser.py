from .cd_converter import CDConverter
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
    def __init__(self, verbLookup, cdConverter:CDConverter):
        self.verbLookup = verbLookup
        self.cdConverter = cdConverter

    def parse_sentence(self, sentence):
        if " emit" in sentence:
            verb_info = self.verbLookup.get_verb('emit')
            action_event = self.cdConverter.convert_verb_event_to_action_event(verb_info) #TODO: what do we actually do with this?
        else:
            raise NotImplementedError