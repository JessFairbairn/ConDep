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
    def __init__(self, verbLookup, cdConverter):
        self.verbLookup = verbLookup
        self.cdConverter = cdConverter

    def parse_sentence(self, sentence):
        if " emit" in sentence:
            verb_info = self.verbLookup.get_verb('emit')
            self.cdConverter.convert_verb_event(verb_info)
        else:
            raise NotImplementedError