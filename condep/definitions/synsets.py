from condep.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper

from condep.action_event import EntityAttributes
from condep.action_event import EntityAttributeOutcomes

from condep.primitives import Primitives

dictionary = dict() # type: Dict[str, object]


##EXPEL


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
_move.sense_id = 'move.v.03'
_move.sense_id = 'move'
_move.affected_attribute = EntityAttributes.position

dictionary['move.v.03'] = _move


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


##MOVE

##PROPEL
