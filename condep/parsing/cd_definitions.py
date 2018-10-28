from condep.primitives import Primitives
from condep.action_event import EntityAttributes
from enum import Enum

class CDDefinition:
    '''Describes a verb in terms of conceptual dependancies'''

    def __init__(self, primitive:Primitives=None):
        self.primitive = primitive

    sense_id = None #type: str
    primitive = None # type: EventType
    object_constraint = None 
    affected_attribute = None # type: EntityAttributes
    attribute_outcome = None # type: EntityAttributeOutcomes

    preceding = None # type: CDDefinitionPredecessorWrapper

    # def __iter__(self):
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr, value

class CDDefinitionPredecessorWrapper:
    'Small wrapper for preceding events'

    applies_to = None
    """subject or object"""

    definition = None  # type: CDDefinition
