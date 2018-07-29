from enum import Enum

class ActionEvent:
    subject = None #TODO: decide if this should be string or object
    # 'Object' in logical sense
    event_object = None #TODO: decide if this should be string or object

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