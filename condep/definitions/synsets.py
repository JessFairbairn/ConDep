from condep.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper

from condep.action_event import EntityAttributes
from condep.action_event import EntityAttributeOutcomes

from condep.primitives import Primitives

dictionary = dict() # type: Dict[str, object]


##EXPEL

_OUTPUT01 = CDDefinition(Primitives.EXPEL)
dictionary['output.v.01'] = _OUTPUT01


##INGEST



_heat = CDDefinition(Primitives.INGEST)
_heat.sense_id = 'heat.01'
_heat.object_override = 'Energy'
_heat.actor_override = 'Object'

_heat.preceding = CDDefinitionPredecessorWrapper()
_heat.preceding.applies_to = 'Subject'
_heat.preceding.definition = CDDefinition(Primitives.EXPEL)

dictionary['heat.v.01'] = _heat

_charge = CDDefinition(Primitives.INGEST)
_charge.object_override = 'Charge'
_charge.actor_override = 'Object'

_charge.preceding = CDDefinitionPredecessorWrapper()
_charge.preceding.applies_to = 'Subject'
_charge.preceding.definition = CDDefinition(Primitives.EXPEL)

dictionary['charge.v.23'] = _charge

_consume = CDDefinition(Primitives.INGEST)
_consume.sense_id = 'consume.v.02'
dictionary['consume.v.02'] = _consume


##PTRANS
_move = CDDefinition(Primitives.PTRANS)
_move.affected_attribute = EntityAttributes.position
dictionary['move.v.01'] = _move
dictionary['move.v.02'] = _move
dictionary['travel.v.01'] = _move
dictionary['go.v.01'] = _move


_FLOW01 = CDDefinition(Primitives.PTRANS)
_FLOW01.object_override = 'Subject'
dictionary['flow.v.01'] = _FLOW01

_RUN06 = CDDefinition(Primitives.PTRANS)
_RUN06.object_override = 'Subject'
dictionary['run.v.06'] = _RUN06


_receive = CDDefinition(Primitives.PTRANS)
_receive.sense_id = 'receive.v.05'
_receive.affected_attribute = EntityAttributes.distance_from_subject
_receive.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['receive.v.05'] = _receive

_CLOSE = CDDefinition(Primitives.PTRANS)
_CLOSE.sense_id = 'close_up.v.01'
_CLOSE.affected_attribute = EntityAttributes.position
_CLOSE.object_override = "part(Object)"
dictionary['close_up.v.01'] = _CLOSE

_APPEAR = CDDefinition(Primitives.PTRANS)
_APPEAR.object_override = 'Subject'
_APPEAR.sense_id = 'appear.v.02'
dictionary['appear.v.02'] = _APPEAR


_SURFACE = CDDefinition(Primitives.PTRANS)
_SURFACE.object_attributes['position_after'] = 'above(Liquid)'
dictionary['surface.v.01'] = _SURFACE

_DROP = CDDefinition(Primitives.PTRANS)
_DROP.actor_override = 'Gravity'
dictionary['drop.v.01'] = _DROP

_EXIST = CDDefinition()
dictionary['exist.v.01'] = _EXIST

_ORBIT = CDDefinition()
dictionary['circle.v.02'] = _ORBIT

_EXIT = CDDefinition(Primitives.EXPEL)
_EXIT.object_override = 'Subject'
_EXIT.actor_override = 'Object'
dictionary['exit.v.01'] = _EXIT


_TURN04 = CDDefinition(Primitives.MOVE)
_TURN04.actor_override = 'Object'

_TURN04.preceding = CDDefinitionPredecessorWrapper()
_TURN04.preceding.definition = CDDefinition(Primitives.PROPEL)
dictionary['turn.v.04'] = _TURN04

##MOVE
_MOVE03 = CDDefinition(Primitives.MOVE)
dictionary['move.v.03'] = _MOVE03

_contract = CDDefinition(Primitives.MOVE)
_contract.sense_id = 'contract'
_contract.affected_attribute = EntityAttributes.radius
_contract.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['contract.v.05'] = _contract
dictionary['contract.v.08'] = _contract
dictionary['narrow.v.01'] = _contract

##PROPEL

_FORCE06 = CDDefinition(Primitives.PTRANS)

_FORCE06.preceding = CDDefinitionPredecessorWrapper()
_FORCE06.preceding.definition = CDDefinition(Primitives.PROPEL)
dictionary['force.v.06'] = _FORCE06
dictionary['force.v.07'] = _FORCE06

_LIGHT01 = CDDefinition(Primitives.PROPEL)
_LIGHT01.object_override = 'Light'

_LIGHT01.affected_attribute = EntityAttributes.distance_from_subject
_LIGHT01.attribute_outcome = EntityAttributeOutcomes.increase

_LIGHT01.object_attributes['position_after'] = 'Object'
dictionary['light.v.01'] = _LIGHT01

_fall = CDDefinition(Primitives.PROPEL)
_fall.affected_attribute = EntityAttributes.distance_from_subject
_fall.attribute_outcome = EntityAttributeOutcomes.decrease
dictionary['fall.v.01'] = _fall

# None

dictionary['slope.v.01'] = CDDefinition()