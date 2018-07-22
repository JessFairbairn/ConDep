from pymunk_cd.CDEvent import CDEvent
from pymunk_cd.EventType import EventType
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition

from pymunk_cd.parsing import primitives
from pymunk_cd.parsing import verbs

class CDConverter:

    def convert_verb_event(self, verb_data:VerbSense):
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]
        

        # get verb definition
        cd_primitive = verbs.dictionary[verb_data.verb_sense_id or verb_data.verb_name].primitive

        # get primitive definition
        prim_definition = primitives.dictionary[cd_primitive]

        return CDEvent(subject.argument, cd_primitive, verb_object.argument)

def _merge_definitions(self, def1:CDDefinition, def2:CDDefinition):
        pass