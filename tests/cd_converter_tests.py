from unittest import mock
import unittest
from pymunk_cd.CDEvent import CDEvent
from pymunk_cd.EventType import EventType

from pymunk_cd.parsing import cd_converter
from pymunk_cd.parsing.NLPParser import NLPParser
from pymunk_cd.parsing.VerbSense import VerbArgumentInstance
from pymunk_cd.parsing.VerbSense import VerbSense


class ReturnsCorrectSubjectAndObject(unittest.TestCase):
    def runTest(self):
        converter = cd_converter.cd_converter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("emit", [arg0, arg1])

        result = converter.convert_verb_event(mock_verb_data)

        self.assertIsInstance(result, CDEvent)
        self.assertEqual(result.subject, arg0.argument, 'should set the correct subject for the cd event')
        self.assertEqual(result.object, arg1.argument, 'should set the correct object for the cd event')

class ReturnsCorrectCDPrimitive(unittest.TestCase):
    def runTest(self):
        converter = cd_converter.cd_converter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("emit", [arg0, arg1])

        result = converter.convert_verb_event(mock_verb_data)

        self.assertEqual(result.event_type, EventType.EXPEL)
        
        
if __name__ == '__main__':
    unittest.main(module='cd_converter_tests')
