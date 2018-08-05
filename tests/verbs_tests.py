from unittest import mock
import unittest

from pymunk_cd.definitions import verbs
from pymunk_cd.parsing.cd_definitions import CDDefinition


class ReturnsCorrectSubjectAndObject(unittest.TestCase):
    def runTest(self):
        result = verbs.dictionary.get('emit')

        self.assertIsInstance(result, CDDefinition)

if __name__ == '__main__':
    unittest.main(module='cd_converter_tests')
