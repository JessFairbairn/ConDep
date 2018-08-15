from .primitives import Primitives
from .utilities import stringify_entity

class CDEvent:

    def __init__(self, prim:Primitives):
        self.primitive = prim or None

    subject = None
    # 'Object' in logical sense
    event_object = None

    affected_attribute = None
    attribute_outcome = None




    def __str__(self):
        string = (stringify_entity(self.subject)
        + ' <=> ' 
        + self.primitive.name)

        if self.event_object:
            string = string  + ' ' + stringify_entity(self.event_object)
            # + '\n'
            # + '\t'+ event.affected_attribute.name                                 
            # + ((' -> ' + event.attribute_outcome.name) if event.attribute_outcome else '')

        return string