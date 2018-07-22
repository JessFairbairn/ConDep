from pymunk_cd.EventType import EventType

from .cd_definitions import *

from typing import Dict

dictionary = dict() # type: Dict[EventType, object]

_EXPEL = CDDefinition(EventType.EXPEL)
_EXPEL.object_constraint = 'kind(raidiation)'
_EXPEL.affected_attribute = EntityAttributes.DISTANCE_FROM_SUBJECT
_EXPEL.attribute_change_polarity = True

dictionary[EventType.EXPEL] = _EXPEL
