from unittest import mock
from unittest.mock import patch
import unittest

from pymunk_cd.action_event import ActionEvent
from pymunk_cd.EventType import EventType

from pymunk_cd.CDManager import CDManager
from pymunk_cd.parsing.VerbSense import VerbArgumentInstance
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition
from pymunk_cd.parsing.cd_definitions import EntityAttributes

from pymunk_cd.parsing import verbs
from pymunk_cd.parsing import primitives


class ReturnsCandidateVerbsForScenario(unittest.TestCase):
    def runTest(self):
        action_event = ActionEvent()
        action_event.subject = 'blah'
        action_event.event_object = 'blah'
        action_event.affected_attribute = EntityAttributes.inside_subject

        result = CDManager.detect_scenarios(action_event)

        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 1, 'Should find at least one candidate verb')
        

        


if __name__ == '__main__':
    unittest.main(module='cd_manager_tests')
