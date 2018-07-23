from pymunk_cd.EventType import EventType
from pymunk_cd.action_event import EntityAttributes

from .cd_definitions import *

from typing import Dict

dictionary = dict() # type: Dict[EventType, object]

_EXPEL = CDDefinition(EventType.EXPEL)
_EXPEL.object_constraint = 'kind(raidiation)'
_EXPEL.affected_attribute = EntityAttributes.inside_subject
_EXPEL.attribute_change_polarity = True

dictionary[EventType.EXPEL] = _EXPEL
dictionary[EventType.MOVE] = CDDefinition(EventType.MOVE)
dictionary[EventType.PTRANS] = CDDefinition(EventType.PTRANS)
dictionary[EventType.INGEST] = CDDefinition(EventType.INGEST)
dictionary[EventType.PROPEL] = CDDefinition(EventType.PROPEL)
