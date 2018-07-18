from pymunk_cd.CDEvent import CDEvent
from pymunk_cd.EventType import EventType
from pymunk_cd.parsing.VerbSense import VerbSense

class cd_converter:

    def convert_verb_event(self, verb_data:VerbSense):
        subject = [arg for arg in verb_data.arguments if arg.type == 'PAG'][0]
        verb_object = [arg for arg in verb_data.arguments if arg.type == 'PPT'][0]
        
        cd_primitive = self.verb_to_primitive(verb_data.verb_name)
        return CDEvent(subject.argument, cd_primitive, verb_object.argument)

    def verb_to_primitive(self, verb:str):         
        if verb == "emit":
            return EventType.EXPEL
        else:
            raise NotImplementedError

