from unittest import mock
import unittest

from pymunk_cd.definitions import verbs
from pymunk_cd.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper


class ReturnsCorrectSubjectAndObject(unittest.TestCase):
    def runTest(self):
        result = verbs.dictionary.get('emit')

        self.assertIsInstance(result, CDDefinition)

class Definitions(unittest.TestCase):
    def test_all_preceding_have_correct_preceding(self):
        for key, value in verbs.dictionary.items():
            prec = value.preceding
            self.assertTrue(prec == None or type(prec) == CDDefinitionPredecessorWrapper,
                'Should be None or a CDDefinitionPredecessorWrapper: ' + key + ' failed')

if __name__ == '__main__':
    unittest.main(module='cd_converter_tests')
