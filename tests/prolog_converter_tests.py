from unittest import mock
from unittest.mock import patch
import unittest

from condep.action_event import EntityAttributes
from condep.action_event import EntityAttributeOutcomes
from condep.cd_event import CDEvent
from condep.primitives import Primitives
from condep.prolog import converter


class ConvertEventToPredicates(unittest.TestCase):
    def test_ReturnsList(self):

        event = CDEvent(Primitives.EXPEL)
        

        result = converter.convert_to_prolog(event)

        self.assertIsInstance(result,list)

        for pred in result:
            self.assertIsInstance(pred, str)

    def test_SetsActorAsPredicate(self):
        event = CDEvent(Primitives.EXPEL)
        event.subject = 'star'

        predicates = converter.convert_to_prolog(event)

        self.assertTrue(
            any(pred.startswith("actorOfEvent(star,") for pred in predicates)
        )

    def test_SetsObjectInPredicate(self):
        event = CDEvent(Primitives.EXPEL)
        event.event_object = 'particle'

        predicates = converter.convert_to_prolog(event)

        self.assertTrue(
            any(pred.startswith("objectOfEvent(particle,") for pred in predicates)
        )

        
class CombinesToFile(unittest.TestCase):
    def test(self):
        predicates = []
        output = converter.output_logtalk_file(predicates)

        self.assertIsInstance(output, str)

    def test_ContainsPredicates(self):
        predicates = ['foo','bar']
        output = converter.output_logtalk_file(predicates)

        for pred in predicates:
            self.assertIn(pred,output)

if __name__ == '__main__':
    unittest.main(module='prolog_converter_tests')
