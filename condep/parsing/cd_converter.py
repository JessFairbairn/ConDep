from condep.action_event import ActionEvent
from condep.cd_event import CDEvent
from condep.primitives import Primitives
from condep.parsing.VerbSense import VerbSense
from condep.parsing.cd_definitions import CDDefinition

from condep.definitions import primitives as primitive_definitions

from condep.definitions import verbs

from condep.prolog import prolog_service

class CDConverter:

    def convert_verb_event_to_cd_event(self, verb_data:VerbSense):
        '''Outputs a CDEvent'''
        
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]

        # get verb definition
        verb_definition = verbs.dictionary[verb_data.verb_sense_id or verb_data.verb_name]
        prim_def = primitive_definitions.dictionary[verb_definition.primitive]

        event = CDConverter._merge_definitions(verb_definition, prim_def)
        try:
            event.subject = subject.argument
        except AttributeError:
            pass
            
        try:
            event.event_object = verb_object.argument
        except AttributeError:
            pass
        #TODO: handle more complex argument types

        if verb_definition.preceding:
            prec_verb_def = verb_definition.preceding
            prec_prim_def = primitive_definitions.dictionary[prec_verb_def.definition.primitive]
            event.preceding = CDConverter._merge_definitions(prec_verb_def.definition, prec_prim_def)

        #TODO: check for missing info
        self._check_missing_info(event)

        return event

    def convert_cd_event_to_action_events(self, cd_event:CDEvent):
        
        subject = cd_event.subject
        event_object = cd_event.event_object

        action_array = []
        fuse = 0
        while cd_event:
            action_array.append(
                self._convert_single_cd_event(cd_event, subject, event_object)
            )
            cd_event = cd_event.preceding

            fuse +=1
            assert fuse < 100

        action_array.reverse()
        return action_array

    @staticmethod
    def _convert_single_cd_event(cd_event, subject, event_object):
        prim_definition = primitive_definitions.dictionary[cd_event.primitive]

        action_event = ActionEvent()

        action_event.affected_attribute = cd_event.affected_attribute or prim_definition.affected_attribute
        action_event.attribute_outcome = cd_event.attribute_outcome or prim_definition.attribute_outcome

        action_event.subject = subject
        action_event.event_object = event_object

        return action_event

    @staticmethod
    def _merge_definitions(verb_definition:CDDefinition, prim_defintition:CDDefinition):
        '''Merges a verb definition with a primitive definition, to output a CDEvent'''

        new_def = CDEvent(prim_defintition.preceding)

        for attr in ['primitive', 'sense_id', 'affected_attribute', 'attribute_outcome']:

            attr_1 = verb_definition.__getattribute__(attr)
            attr_2 = prim_defintition.__getattribute__(attr)

            if attr_1 and attr_2 and (attr_1 != attr_2):
                raise ValueError('Conflicting values of ' + attr)
            else:
                explicit_value = verb_definition.__getattribute__(attr)
                setattr(new_def, attr, explicit_value)
            

        return new_def

    @staticmethod
    def _check_missing_info(event:CDEvent):
        if not event.subject:
            if event.primitive == Primitives.EXPEL or event.primitive == Primitives.INGEST:
                prolog_service.query_prolog(event)