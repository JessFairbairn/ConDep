from condep.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper

from condep.action_event import EntityAttributes
from condep.action_event import EntityAttributeOutcomes

from condep.primitives import Primitives

dictionary = dict() # type: Dict[str, object]


##EXPEL
_emit = CDDefinition(Primitives.EXPEL)
_emit.sense_id = 'emit'
_emit.object_override = 'kind(raidiation)'
_emit.affected_attribute = EntityAttributes.inside_subject
_emit.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['emit'] = _emit

_eject = CDDefinition(Primitives.EXPEL)
_eject.sense_id = 'eject'
_eject.affected_attribute = EntityAttributes.inside_subject
_eject.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['eject'] = _eject

##INGEST
_absorb = CDDefinition(Primitives.INGEST)
_absorb.sense_id = 'absorb'
_absorb.affected_attribute = EntityAttributes.inside_subject
_absorb.attribute_outcome = EntityAttributeOutcomes.inside

dictionary['absorb'] = _absorb

_fall = CDDefinition(Primitives.INGEST)
_fall.sense_id = 'fall'

_fall.preceding = CDDefinitionPredecessorWrapper()
_fall.preceding.definition = CDDefinition(Primitives.PROPEL)
_fall.preceding.definition.affected_attribute = EntityAttributes.distance_from_subject
_fall.preceding.definition.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['fall'] = _fall


_heat = CDDefinition(Primitives.INGEST)
_heat.sense_id = 'heat.01'
_heat.object_override = 'Energy'

_heat.preceding = CDDefinitionPredecessorWrapper()
_heat.preceding.applies_to = 'Subject'
_heat.preceding.definition = CDDefinition(Primitives.EXPEL)

dictionary['heat'] = _heat

##PTRANS
_move = CDDefinition(Primitives.PTRANS)
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.position

dictionary['move'] = _move


_escape = CDDefinition(Primitives.PTRANS)
_escape.sense_id = 'escape'
_escape.affected_attribute = EntityAttributes.position

dictionary['escape'] = _escape


##MOVE
_contract = CDDefinition(Primitives.MOVE)
_contract.sense_id = 'contract'
_contract.affected_attribute = EntityAttributes.radius
_contract.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['contract'] = _contract

_collapse = CDDefinition(Primitives.MOVE)
_collapse.sense_id = 'collapse'
_collapse.affected_attribute = EntityAttributes.radius
_collapse.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['collapse'] = _collapse

_EXPAND = CDDefinition(Primitives.MOVE)
_EXPAND.sense_id = 'expand'
_EXPAND.affected_attribute = EntityAttributes.radius
_EXPAND.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['expand'] = _EXPAND

_GORGE = CDDefinition(Primitives.MOVE)
_GORGE.sense_id = 'gorge'
_GORGE.affected_attribute = EntityAttributes.radius
_GORGE.attribute_outcome = EntityAttributeOutcomes.increase
_GORGE.preceding = CDDefinitionPredecessorWrapper()
_GORGE.preceding.definition = CDDefinition(Primitives.INGEST)
dictionary['gorge'] = _GORGE

_ACCRETE = CDDefinition(Primitives.MOVE)
_ACCRETE.sense_id = 'accrete'
_ACCRETE.affected_attribute = EntityAttributes.radius
_ACCRETE.attribute_outcome = EntityAttributeOutcomes.increase

_ACCRETE.preceding = CDDefinitionPredecessorWrapper()
_ACCRETE.preceding.definition = CDDefinition(Primitives.INGEST)
dictionary['accrete'] = _ACCRETE

##PROPEL
_ACCELERATE = CDDefinition(Primitives.PROPEL)
_ACCELERATE.sense_id = 'accelerate'
_ACCELERATE.affected_attribute = EntityAttributes.velocity
_ACCELERATE.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['accelerate'] = _ACCELERATE

_DECELERATE = CDDefinition(Primitives.PROPEL)
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