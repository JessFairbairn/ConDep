import unittest
from condep.parsing.NLPParser import VerbLookup
from condep.parsing import VerbSense


# class unittest.TestCase(unittest.TestCase):    
#     def setUpClass(self):
#         self.verb_lookup = VerbLookup()

class TakesInputSentence(unittest.TestCase):
    'For testing basic input processing'

    def runTest(self):
        VerbLookup().get_verb('emit')
        return

class ReturnsVerbSenseObject(unittest.TestCase):
    def runTest(self):
        result = VerbLookup().get_verb('emit')
        self.assertIsInstance(result, VerbSense.VerbSense)

class ReturnsCorrectVerb(unittest.TestCase):
    def runTest(self):
        result = VerbLookup().get_verb('emit')
        self.assertEqual(result.verb_name, 'emit')

class ArgumentsAreCorrectClass(unittest.TestCase):
    def runTest(self):
        result = VerbLookup().get_verb('emit')
        self.assertIsInstance(result.arguments, list)
        self.assertGreater(len(result.arguments), 0, 'Should have verb arguments')
        self.assertTrue(
            all(isinstance(arg, VerbSense.VerbArgument) for arg in result.arguments),
            'Should be verb argument class')


if __name__ == '__main__':
    unittest.main(module='NLPParser_tests')
