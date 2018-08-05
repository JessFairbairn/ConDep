from pymunk_cd.primitives import Primitives
from pymunk_cd.action_event import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes

from .cd_definitions import *

from typing import Dict

dictionary = dict() # type: Dict[EventType, object]

_EXPEL = CDDefinition(Primitives.EXPEL)
_EXPEL.affected_attribute = EntityAttributes.inside_subject
_EXPEL.attribute_outcome = EntityAttributeOutcomes.outside
dictionary[Primitives.EXPEL] = _EXPEL

_ptrans = CDDefinition(Primitives.PTRANS)
_ptrans.affected_attribute = EntityAttributes.position
dictionary[Primitives.PTRANS] = _ptrans

_propel = CDDefinition(Primitives.PROPEL)
_propel.affected_attribute = EntityAttributes.velocity
dictionary[Primitives.PROPEL] = _propel

_INGEST = CDDefinition(Primitives.INGEST)
_INGEST.affected_attribute = EntityAttributes.inside_subject
_INGEST.attribute_outcome = EntityAttributeOutcomes.inside
dictionary[Primitives.INGEST] = _INGEST

_MOVE = CDDefinition(Primitives.MOVE)
_MOVE.affected_attribute = EntityAttributes.radius
#TODO: replace 'radius' with a 'part of subject' type constraint
dictionary[Primitives.MOVE] = _MOVE

