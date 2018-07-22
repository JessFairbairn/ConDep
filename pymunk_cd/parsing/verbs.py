from .cd_definitions import *

dictionary = dict() # type: Dict[str, object]

_emit = CDDefinition(EventType.EXPEL)
_emit.sense_id = 'emit'
_emit.object_constraint = 'kind(raidiation)'
_emit.affected_attribute = EntityAttributes.DISTANCE_FROM_SUBJECT
_emit.attribute_change_polarity = True

dictionary['emit'] = _emit
