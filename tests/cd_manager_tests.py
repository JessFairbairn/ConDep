from unittest import mock
from unittest.mock import patch
import unittest

from pymunk_cd.action_event import ActionEvent
from pymunk_cd.EventType import EventType
from pymunk_cd.CDManager import CDManager
from pymunk_cd.CompoundEntity import CompoundEntity

from pymunk_cd.parsing.cd_definitions import CDDefinition
from pymunk_cd.parsing.cd_definitions import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes

from pymunk_cd.parsing import verbs
from pymunk_cd.parsing import primitives


class ReturnsCandidateVerbsForScenario(unittest.TestCase):
    def runTest(self):
        action_event = ActionEvent()
        action_event.subject = 'blah'
        action_event.event_object = 'blah'
        action_event.affected_attribute = EntityAttributes.radius
        action_event.attribute_outcome = EntityAttributeOutcomes.increase

        result = CDManager.detect_scenarios(action_event)

        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 1, 'Should find at least one candidate verb')

class GetEntityIndex(unittest.TestCase):

    def runTest(self):
        ent1 = CompoundEntity()
        ent2 = CompoundEntity()
        ent2.name = 'target entity'

        manager = CDManager(None, None)

        manager.objects.append(ent1)
        manager.objects.append(ent2)

        index = manager.get_entity_index(ent2)

        self.assertEqual(index, 1)

if __name__ == '__main__':
    unittest.main(module='cd_manager_tests')
