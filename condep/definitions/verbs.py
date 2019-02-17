from condep.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper

from condep.action_event import EntityAttributes
from condep.action_event import EntityAttributeOutcomes

from condep.primitives import Primitives

dictionary = dict() # type: Dict[str, object]


##EXPEL
_emit = CDDefinition(Primitives.EXPEL)
_emit.sense_id = 'emit'
_emit.object_override = 'kind(radiation)'
_emit.affected_attribute = EntityAttributes.inside_subject
_emit.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['emit'] = _emit

_eject = CDDefinition(Primitives.EXPEL)
_eject.sense_id = 'eject'
_eject.affected_attribute = EntityAttributes.inside_subject
_eject.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['eject'] = _eject

_leave = CDDefinition(Primitives.EXPEL)

_leave.preceding = CDDefinitionPredecessorWrapper()
_leave.preceding.definition = CDDefinition(Primitives.PTRANS)
_leave.preceding.definition.affected_attribute = EntityAttributes.distance_from_subject
_leave.preceding.definition.attribute_outcome = EntityAttributeOutcomes.increase

_leave.sense_id = 'leave'
_leave.affected_attribute = EntityAttributes.inside_subject
_leave.attribute_outcome = EntityAttributeOutcomes.outside

dictionary['leave'] = _leave

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
_heat.actor_override = 'Object'

_heat.preceding = CDDefinitionPredecessorWrapper()
_heat.preceding.applies_to = 'Subject'
_heat.preceding.definition = CDDefinition(Primitives.EXPEL)

dictionary['heat'] = _heat

_charge = CDDefinition(Primitives.INGEST)
_charge.sense_id = 'charge.03'
_charge.object_override = 'Charge'
_charge.actor_override = 'Object'

_charge.preceding = CDDefinitionPredecessorWrapper()
_charge.preceding.applies_to = 'Subject'
_charge.preceding.definition = CDDefinition(Primitives.EXPEL)

dictionary['charge'] = _charge

_consume = CDDefinition(Primitives.INGEST)
_consume.sense_id = 'consume.v.02'
dictionary['consume'] = _consume

_take = CDDefinition(Primitives.INGEST)
_take.preceding = CDDefinitionPredecessorWrapper()
_take.preceding.definition = CDDefinition(Primitives.PTRANS)
_take.preceding.definition.affected_attribute =   EntityAttributes.distance_from_subject

_take.preceding.definition.attribute_outcome =    EntityAttributeOutcomes.decrease
dictionary['take'] = _take

_enter = CDDefinition(Primitives.INGEST)
_enter.actor_override = 'Container'
_enter.object_override = 'Subject'

_enter.preceding = CDDefinitionPredecessorWrapper()
_enter.preceding.applies_to = 'Subject'
_enter.preceding.definition = CDDefinition(Primitives.PTRANS)
_enter.preceding.definition.affected_attribute =   EntityAttributes.distance_from_subject
_enter.preceding.definition.attribute_outcome =    EntityAttributeOutcomes.decrease
dictionary['enter'] = _enter

##PTRANS
_move = CDDefinition(Primitives.PTRANS)
_move.sense_id = 'move.v.02'
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.position

dictionary['move'] = _move
dictionary['move.v.03'] = _move

dictionary['displace'] = _move

_escape = CDDefinition(Primitives.PTRANS)
_escape.sense_id = 'escape'
_escape.affected_attribute = EntityAttributes.position

dictionary['escape'] = _escape


_receive = CDDefinition(Primitives.PTRANS)
_receive.sense_id = 'receive.v.05'
_receive.affected_attribute = EntityAttributes.distance_from_subject
_receive.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['receive'] = _receive

_collide = CDDefinition(Primitives.PTRANS)
_collide.affected_attribute = EntityAttributes.distance_from_subject
_collide.attribute_outcome = EntityAttributeOutcomes.zero
dictionary['collide'] = _collide

_meet = CDDefinition(Primitives.PTRANS)
_meet.affected_attribute = EntityAttributes.distance_from_subject
_meet.attribute_outcome = EntityAttributeOutcomes.zero
dictionary['meet'] = _meet

_give = CDDefinition(Primitives.PTRANS)
_give.affected_attribute = EntityAttributes.distance_from_subject
_give.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['give'] = _give

_CLOSE = CDDefinition(Primitives.PTRANS)
_CLOSE.sense_id = 'close_up.v.01'
_CLOSE.affected_attribute = EntityAttributes.position
_CLOSE.object_override = "part(Object)"
dictionary['close'] = _CLOSE

_LOSE = CDDefinition(Primitives.PTRANS)
_LOSE.affected_attribute = EntityAttributes.distance_from_subject
_LOSE.object_override = "part(Subject)"
dictionary['lose'] = _LOSE

_ARRIVE = CDDefinition(Primitives.PTRANS)
_ARRIVE.object_override = 'Subject'
dictionary['arrive'] = _ARRIVE

_APPEAR = CDDefinition(Primitives.PTRANS)
_APPEAR.object_override = 'Subject'
_APPEAR.sense_id = 'appear.v.02'
dictionary['appear'] = _APPEAR

_INSTALL = CDDefinition(Primitives.PTRANS)
dictionary['install'] = _INSTALL


_PRESSURIZE = CDDefinition(Primitives.PTRANS)
_PRESSURIZE.object_override = 'kind(Fluid)'
_PRESSURIZE.object_attributes['position_after'] = 'inside(Object)'
dictionary['pressurize'] = _PRESSURIZE


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

_grow = CDDefinition(Primitives.MOVE)
_grow.sense_id = 'grow'
_grow.affected_attribute = EntityAttributes.radius
_grow.attribute_outcome = EntityAttributeOutcomes.increase
dictionary['grow'] = _grow

_GORGE = CDDefinition(Primitives.MOVE)
_GORGE.sense_id = 'gorge'
_GORGE.affected_attribute = EntityAttributes.radius
_GORGE.attribute_outcome = EntityAttributeOutcomes.increase
_GORGE.preceding = CDDefinitionPredecessorWrapper()
_GORGE.preceding.definition = CDDefinition(Primitives.INGEST)
dictionary['gorge'] = _GORGE

_ACCRETE = CDDefinition(Primitives.MOVE)
_ACCRETE.affected_attribute = EntityAttributes.radius
_ACCRETE.attribute_outcome = EntityAttributeOutcomes.increase
_ACCRETE.object_override = 'Radius'

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
# deform
# reflect
# form
# friction