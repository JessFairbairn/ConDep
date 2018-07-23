from .cd_definitions import *

from pymunk_cd.action_event import EntityAttributes

dictionary = dict() # type: Dict[str, object]

_emit = CDDefinition(EventType.EXPEL)
_emit.sense_id = 'emit'
_emit.object_constraint = 'kind(raidiation)'
_emit.affected_attribute = EntityAttributes.distance_from_subject
_emit.attribute_change_polarity = True

dictionary['emit'] = _emit
