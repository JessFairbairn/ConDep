import sys

import nltk
import spacy
from spacy import displacy
from spacy.symbols import dobj, nsubj, nsubjpass, pobj, prep, VERB

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
        

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(sentence)


        sents = list(doc.sents)
        if len(sents) > 1:
            print("Can only process single sentences.", file=sys.stderr)
            exit(1)

        root = sents[0].root

        # stem verb
        stemmer = nltk.stem.PorterStemmer()

        verb_info = self.verbLookup.get_verb(stemmer.stem(str(root)))

        subject = None
        obj = None
        for child in root.children:
            if child.dep == nsubj:
                subject = child
            elif child.dep == dobj or child.dep == nsubjpass:
                obj = child
            elif child.dep == prep:
                try:
                    propbank_tag = self.preposition_to_propbank[str(child)]
                except KeyError:
                    propbank_tag = 'PPT'
                
                for prop_child in child.children:
                    if prop_child.dep == pobj:
                        verb_info.set_argument_by_type(propbank_tag, str(prop_child))
        
        
        if obj:
            verb_info.get_verb_object().argument = str(obj)
        
        verb_info.get_verb_subject().argument = str(subject)

        # TODO: extract and encode preposition info
        # elif len(pos_tags) > 3:
        #     prepositions = list(map(lambda tuple: tuple[0], filter(lambda tuple: tuple[1] == 'IN', pos_tags)))
        #     if len(prepositions) > 1:
        #         raise NotImplementedError('Too many prepositions')
        #     elif not prepositions:
        #         raise NotImplementedError('Sentence is too complex to process sorry :(')

        #     index = stripped_words.index(prepositions[0])
        #     location = stripped_words[index + 1]

        #     
            

        return self.cdConverter.convert_verb_event_to_cd_event(verb_info)
        
    preposition_to_propbank = {
        'from': 'DIR',
        'into': 'GOL'
        }