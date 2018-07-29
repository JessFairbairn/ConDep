from pymunk_cd.EventType import EventType
from pymunk_cd.action_event import EntityAttributes
from enum import Enum

class CDDefinition:
    '''Describes a verb in terms of conceptual dependancies'''

    def __init__(self, primitive:EventType=None):
        self.primitive = primitive

    sense_id = None
    primitive = None # type: EventType
    object_constraint = None 
    affected_attribute = None # type: EntityAttributes
    attribute_outcome = None # type: Boolean

    # def __iter__(self):
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr, value
