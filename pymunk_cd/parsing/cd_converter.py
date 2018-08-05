from pymunk_cd.action_event import ActionEvent
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.primitives import Primitives
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition

from pymunk_cd.parsing import primitives
from pymunk_cd.parsing import verbs

class CDConverter:

    def convert_verb_event_to_cd_event(self, verb_data:VerbSense):
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]

        # get verb definition
        verb_definition = verbs.dictionary[verb_data.verb_sense_id or verb_data.verb_name]

        event = CDEvent(verb_definition.primitive)
        event.subject = subject.argument
        event.event_object = verb_object.argument
        return event

    def convert_cd_event_to_action_event(self, cd_event:CDEvent):
        action_event = ActionEvent()

        prim_definition = primitives.dictionary[cd_event.primitive]

        action_event.affected_attribute = prim_definition.affected_attribute
        action_event.attribute_outcome = prim_definition.attribute_outcome

        action_event.subject = cd_event.subject
        action_event.event_object = cd_event.event_object

        return action_event

    