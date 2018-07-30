from .cd_definitions import *

from pymunk_cd.action_event import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes

dictionary = dict() # type: Dict[str, object]


##EXPEL
_emit = CDDefinition(EventType.EXPEL)
_emit.sense_id = 'emit'
_emit.object_constraint = 'kind(raidiation)'
_emit.affected_attribute = EntityAttributes.inside_subject
_emit.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['emit'] = _emit

_eject = CDDefinition(EventType.EXPEL)
_eject.sense_id = 'eject'
_eject.affected_attribute = EntityAttributes.inside_subject
_eject.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['eject'] = _eject

##INGEST
_absorb = CDDefinition(EventType.INGEST)
_absorb.sense_id = 'absorb'
_absorb.affected_attribute = EntityAttributes.inside_subject
_absorb.attribute_outcome = EntityAttributeOutcomes.inside

dictionary['absorb'] = _absorb


##PTRANS
_move = CDDefinition(EventType.PTRANS)
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.position

dictionary['move'] = _move


##MOVE
_contract = CDDefinition(EventType.MOVE)
_contract.sense_id = 'contract'
_contract.affected_attribute = EntityAttributes.radius
_contract.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['contract'] = _contract

_collapse = CDDefinition(EventType.MOVE)
_collapse.sense_id = 'collapse'
_collapse.affected_attribute = EntityAttributes.radius
_collapse.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['collapse'] = _collapse

_EXPAND = CDDefinition(EventType.MOVE)
_EXPAND.sense_id = 'expand'
_EXPAND.affected_attribute = EntityAttributes.radius
_EXPAND.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['expand'] = _EXPAND

##PROPEL
_ACCELERATE = CDDefinition(EventType.PROPEL)
_ACCELERATE.sense_id = 'accelerate'
_ACCELERATE.affected_attribute = EntityAttributes.velocity
_ACCELERATE.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['accelerate'] = _ACCELERATE

_DECELERATE = CDDefinition(EventType.PROPEL)
_DECELERATE.sense_id = 'decelerate'
_DECELERATE.affected_attribute = EntityAttributes.velocity
_DECELERATE.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['decelerate'] = _DECELERATE

# TODO:
# escape
# deform
# reflect
# form
# grow
# fall
# heat
# friction