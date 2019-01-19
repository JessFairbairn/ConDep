import sys

import nltk

from condep.parsing.cd_converter import CDConverter
from .VerbSense import VerbArgument, VerbSense

import condep.utilities as utilities

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
        

        words = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(words)

        if pos_tags[-1][1] == '.':
            words = words[0:-1]
            pos_tags = pos_tags[0:-1]

        # check for passive voice
        passive_voice = False
        for i in range(0, len(pos_tags) - 1):
            tup = pos_tags[i]
            if tup[0] == 'is' and pos_tags[i+1][1] == 'VBN':
                passive_voice = True
                break

        if passive_voice:
            verbs = list(filter(lambda tuple: tuple[1].startswith('VB') and tuple[0] != 'is', pos_tags))
        else:
            verbs = list(filter(lambda tuple: tuple[1].startswith('VB'), pos_tags))

        if len(verbs) == 1:
            verb = verbs[0][0]
        elif len(verbs) == 0:
            verb = pos_tags[1][0]
            utilities.warn('No verbs found, guessing '+ verb + ' is verb')
        else:
            raise NotImplementedError('Multiple verbs found')
        


        # stem verb
        stemmer = nltk.stem.PorterStemmer()

        verb_info = self.verbLookup.get_verb(stemmer.stem(verb))


        pos_tags = list(filter(lambda tuple: tuple, filter(lambda tuple: tuple[1] != 'DT', pos_tags)))
        stripped_words = list(map(lambda pos: pos[0],pos_tags))
        
        if passive_voice:
            verb_info.get_verb_object().argument = stripped_words[0]
        else:
            verb_info.get_verb_subject().argument = stripped_words[0]


        if len(pos_tags) == 3:
            verb_info.get_verb_object().argument = pos_tags[2][0]
        elif len(pos_tags) > 3:
            prepositions = list(map(lambda tuple: tuple[0], filter(lambda tuple: tuple[1] == 'IN', pos_tags)))
            if len(prepositions) > 1:
                raise NotImplementedError('Too many prepositions')
            elif not prepositions:
                raise NotImplementedError('Sentence is too complex to process sorry :(')

            index = stripped_words.index(prepositions[0])
            location = stripped_words[index + 1]

            try:
                propbank_tag = self.preposition_to_propbank[prepositions[0]]
            except KeyError:
                propbank_tag = 'PPT'
                
            verb_info.set_argument_by_type(propbank_tag, location)
            

        return self.cdConverter.convert_verb_event_to_cd_event(verb_info)
        
    preposition_to_propbank = {
        'from': 'DIR',
        'into': 'GOL'
        }