from .cd_definitions import *

from pymunk_cd.action_event import EntityAttributes

dictionary = dict() # type: Dict[str, object]

_emit = CDDefinition(EventType.EXPEL)
_emit.sense_id = 'emit'
_emit.object_constraint = 'kind(raidiation)'
_emit.affected_attribute = EntityAttributes.inside_subject
_emit.attribute_change_polarity = False

dictionary['emit'] = _emit

_eject = CDDefinition(EventType.EXPEL)
_eject.sense_id = 'eject'
_eject.affected_attribute = EntityAttributes.inside_subject
_eject.attribute_change_polarity = False

dictionary['eject'] = _eject

_move = CDDefinition(EventType.PTRANS)
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.inside_subject
_move.attribute_change_polarity = False

dictionary['move'] = _move

_contract = CDDefinition(EventType.MOVE)
_contract.sense_id = 'contract'
_contract.affected_attribute = EntityAttributes.radius
_contract.attribute_change_polarity = False

dictionary['contract'] = _contract