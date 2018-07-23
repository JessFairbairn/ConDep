from enum import Enum

class ActionEvent:
    subject = None #TODO: decide if this should be string or object
    # 'Object' in logical sense
    event_object = None #TODO: decide if this should be string or object

    affected_attribute = None # type: EntityAttributes
    attribute_change_polarity = None # type: Boolean

class EntityAttributes(Enum):
    inside_subject = 1
    distance_from_subject = 2
    radius = 3
    velocity = 4
    momentum = 5
    position= 6