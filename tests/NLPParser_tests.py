from unittest import mock
import unittest
from pymunk_cd.parsing import NLPParser
from pymunk_cd.parsing.NLPParser import NLPParser
from pymunk_cd.parsing.VerbSense import *

class PassesVerbDataToCDConverter(unittest.TestCase):

    @mock.patch('pymunk_cd.parsing.cd_converter.CDConverter')
    @mock.patch('pymunk_cd.parsing.NLPParser.VerbLookup')
    def test_passes_verb_data_to_converter(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('Black holes emit hawking raidiation.')

        mockCDConverter.convert_verb_event_to_cd_event.assert_called_once_with(mock_verb_data)

    @mock.patch('pymunk_cd.parsing.cd_converter.CDConverter')
    @mock.patch('pymunk_cd.parsing.NLPParser.VerbLookup')
    def test_converts_verb_to_infinitive(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('Star emits particle')

        mockVerbLookup.get_verb.assert_called_once_with('emit')
        