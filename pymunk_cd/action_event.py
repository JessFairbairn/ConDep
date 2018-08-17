from enum import Enum
import typing

#from pymunk_cd.CompoundEntity import CompoundEntity

class ActionEvent:
    subject = None # type!: typing.Union[CompoundEntity, str]
    
    event_object = None # type!: typing.Union[CompoundEntity, str]
    ''''Object' in logical sense'''

    affected_attribute = None # type: EntityAttributes
    attribute_outcome = None # type: EntityAttributeOutcomes

class EntityAttributes(Enum):
    inside_subject = 1
    distance_from_subject = 2
    radius = 3
    velocity = 4
    position= 5

class EntityAttributeOutcomes(Enum):
    inside = 1
    outside = 2

    increase = 3
    decrease = 4