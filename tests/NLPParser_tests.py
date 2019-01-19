from unittest import mock
import unittest
from condep.parsing import NLPParser
from condep.parsing.NLPParser import NLPParser
from condep.parsing.VerbSense import *

class PassesVerbDataToCDConverter(unittest.TestCase):

    @mock.patch('condep.parsing.cd_converter.CDConverter')
    @mock.patch('condep.parsing.NLPParser.VerbLookup')
    def test_passes_verb_data_to_converter(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('Star emits raidiation')

        mockCDConverter.convert_verb_event_to_cd_event.assert_called_once_with(mock_verb_data)

    @mock.patch('condep.parsing.cd_converter.CDConverter')
    @mock.patch('condep.parsing.NLPParser.VerbLookup')
    def test_converts_verb_to_infinitive(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('Star emits particle')

        mockVerbLookup.get_verb.assert_called_once_with('emit')
        
    @mock.patch('condep.parsing.cd_converter.CDConverter')
    @mock.patch('condep.parsing.NLPParser.VerbLookup')
    def test_removes_full_stops(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('Star absorbs raidiation.')

        mockCDConverter.convert_verb_event_to_cd_event.assert_called_once_with(mock_verb_data)

class PassiveVoiceProcessingTests(unittest.TestCase):

    @mock.patch('condep.parsing.cd_converter.CDConverter')
    @mock.patch('condep.parsing.NLPParser.VerbLookup')
    def test_gets_object_correctly(self, mockVerbLookup, mockCDConverter):

        arg0 = VerbArgument('emitting entity', 'PAG')
        arg1 = VerbArgument('thing emitted', 'PPT')
        mock_verb_data = VerbSense("emit", [arg0, arg1])
        mockVerbLookup.get_verb.return_value = mock_verb_data

        parser = NLPParser(mockVerbLookup, mockCDConverter)
        parser.parse_sentence('A rock is ejected from a star')

        passed_verb_data = mockCDConverter.convert_verb_event_to_cd_event.call_args_list[0][0][0] # type: VerbSense
        self.assertEqual(passed_verb_data.get_verb_object().argument, 'rock')
        pass

if __name__ == "__main__":
    unittest.main()