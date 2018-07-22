from pymunk_cd.EventType import EventType
from enum import Enum

class CDDefinition:
    '''Describes a verb in terms of conceptual dependancies'''

    def __init__(self, primitive:EventType=None):
        self.primitive = primitive

    sense_id = None
    primitive = None # type: EventType
    object_constraint = None 
    affected_attribute = None # type: EntityAttributes
    attribute_change_polarity = None # type: Boolean

    # def __iter__(self):
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr, value

class EntityAttributes(Enum):
    RADIUS = 1
    VELOCITY = 2
    DISTANCE_FROM_SUBJECT = 3