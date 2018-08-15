from pymunk_cd.action_event import ActionEvent
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.primitives import Primitives
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition

from pymunk_cd.definitions import primitives as primitive_definitions

from pymunk_cd.definitions import verbs

class CDConverter:

    def convert_verb_event_to_cd_event(self, verb_data:VerbSense):
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]

        # get verb definition
        verb_definition = verbs.dictionary[verb_data.verb_sense_id or verb_data.verb_name]
        prim_def = primitive_definitions.dictionary[verb_definition.primitive]

        event = CDConverter._check_compatible(verb_definition, prim_def)
        event.subject = subject.argument
        try:
            event.event_object = verb_object.argument
        except AttributeError:
            pass

        return event

    def convert_cd_event_to_action_event(self, cd_event:CDEvent):        

        prim_definition = primitive_definitions.dictionary[cd_event.primitive]

        action_event = ActionEvent()

        action_event.affected_attribute = cd_event.affected_attribute or prim_definition.affected_attribute
        action_event.attribute_outcome = cd_event.attribute_outcome or prim_definition.attribute_outcome

        action_event.subject = cd_event.subject
        action_event.event_object = cd_event.event_object

        return action_event

    @staticmethod
    def _check_compatible(verb_definition:CDDefinition, prim_defintition:CDDefinition):
        new_def = CDEvent

        for attr in ['primitive', 'sense_id', 'affected_attribute', 'attribute_outcome']:

            attr_1 = verb_definition.__getattribute__(attr)
            attr_2 = prim_defintition.__getattribute__(attr)

            if attr_1 and attr_2 and (attr_1 != attr_2):
                raise ValueError('Conflicting values of ' + attr)
            else:
                explicit_value = verb_definition.__getattribute__(attr)
                setattr(new_def, attr, explicit_value)
            

        return new_def