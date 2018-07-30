from pymunk_cd.EventType import EventType
from pymunk_cd.action_event import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes

from .cd_definitions import *

from typing import Dict

dictionary = dict() # type: Dict[EventType, object]

_EXPEL = CDDefinition(EventType.EXPEL)
_EXPEL.affected_attribute = EntityAttributes.inside_subject
_EXPEL.attribute_outcome = EntityAttributeOutcomes.outside
dictionary[EventType.EXPEL] = _EXPEL

_ptrans = CDDefinition(EventType.PTRANS)
_ptrans.affected_attribute = EntityAttributes.position
dictionary[EventType.PTRANS] = _ptrans

_propel = CDDefinition(EventType.PROPEL)
_propel.affected_attribute = EntityAttributes.velocity
dictionary[EventType.PROPEL] = _propel

_INGEST = CDDefinition(EventType.INGEST)
_INGEST.affected_attribute = EntityAttributes.inside_subject
_INGEST.attribute_outcome = EntityAttributeOutcomes.inside
dictionary[EventType.INGEST] = _INGEST

dictionary[EventType.MOVE] = CDDefinition(EventType.MOVE)

