from pymunk_cd.action_event import ActionEvent
from pymunk_cd.CDEvent import CDEvent
from pymunk_cd.EventType import EventType
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition

from pymunk_cd.parsing import primitives
from pymunk_cd.parsing import verbs

class CDConverter:

    def convert_verb_event_to_action_event(self, verb_data:VerbSense):
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]        

        # get verb definition
        verb_definition = verbs.dictionary[verb_data.verb_sense_id or verb_data.verb_name]

        # get primitive definition
        prim_definition = primitives.dictionary[verb_definition.primitive]

        merged_definition = _merge_definitions(verb_definition, prim_definition)

        event = ActionEvent()
        event.affected_attribute = merged_definition.affected_attribute
        event.attribute_change_polarity = merged_definition.attribute_change_polarity
        event.subject = subject.argument
        event.event_object = verb_object.argument

        return event #CDEvent(subject.argument, merged_definition.primitive, verb_object.argument)

def _merge_definitions(def1:CDDefinition, def2:CDDefinition):
        new_def = def1

        for attr in ['primitive', 'sense_id', 'affected_attribute', 'object_constraint', 'attribute_change_polarity']:
            
            attr_1 = def1.__getattribute__(attr)
            attr_2 = def2.__getattribute__(attr)

            # TODO: handle attribute_change_polarity better as it's boolean
            if attr_1 and attr_2 and (attr_1 != attr_2):
                raise ValueError('Conflicting values of ' + attr)
            else:
                new_def.__setattr__(attr, def1.__getattribute__(attr) or def2.__getattribute__(attr))

        return new_def