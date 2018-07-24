from .cd_definitions import *

from pymunk_cd.action_event import EntityAttributes

dictionary = dict() # type: Dict[str, object]


##EXPEL
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

##INGEST
_absorb = CDDefinition(EventType.INGEST)
_absorb.sense_id = 'absorb'
_absorb.affected_attribute = EntityAttributes.inside_subject
_absorb.attribute_change_polarity = False

dictionary['absorb'] = _absorb


##PTRANS
_move = CDDefinition(EventType.PTRANS)
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.position
_move.attribute_change_polarity = False

dictionary['move'] = _move


##MOVE
_contract = CDDefinition(EventType.MOVE)
_contract.sense_id = 'contract'
_contract.affected_attribute = EntityAttributes.radius
_contract.attribute_change_polarity = False

dictionary['contract'] = _contract

_collapse = CDDefinition(EventType.MOVE)
_collapse.sense_id = 'collapse'
_collapse.affected_attribute = EntityAttributes.radius
_collapse.attribute_change_polarity = False

dictionary['collapse'] = _collapse

# TODO:
# escape
# deform
# reflects
# form
# collapse
# grow
# falls
# heated
# friction