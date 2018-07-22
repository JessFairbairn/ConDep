from unittest import mock
from unittest.mock import patch
import unittest
from pymunk_cd.CDEvent import CDEvent
from pymunk_cd.EventType import EventType

from pymunk_cd.parsing import cd_converter
from pymunk_cd.parsing.NLPParser import NLPParser
from pymunk_cd.parsing.VerbSense import VerbArgumentInstance
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition
from pymunk_cd.parsing.cd_definitions import EntityAttributes

from pymunk_cd.parsing import verbs
from pymunk_cd.parsing import primitives


class ReturnsCorrectSubjectAndObject(unittest.TestCase):
    def runTest(self):
        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("emit", [arg0, arg1])

        result = converter.convert_verb_event(mock_verb_data)

        self.assertIsInstance(result, CDEvent)
        self.assertEqual(result.subject, arg0.argument,
                         'should set the correct subject for the cd event')
        self.assertEqual(result.event_object, arg1.argument,
                         'should set the correct object for the cd event')


class ReturnsCorrectCDPrimitive(unittest.TestCase):
    def runTest(self):
        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("emit", [arg0, arg1])

        result = converter.convert_verb_event(mock_verb_data)

        self.assertEqual(result.event_type, EventType.EXPEL)


class CallsVerbDictionary(unittest.TestCase):
    @unittest.skip
    def runTest(self):
        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("spew", [arg0, arg1])

        my_dict = {'spew': CDDefinition(EventType.EXPEL)}

        def getitem(name):
            return my_dict[name]

        mock_dictionary = mock.MagicMock()
        mock_dictionary.__getitem__.side_effect = getitem
        with patch('verbs.dictionary', new=mock_dictionary):
            # verbs.dictionary = mock_dictionary

            converter.convert_verb_event(mock_verb_data)

            mock_dictionary.__getitem__.assert_any_call('spew')


class CallsPrimitiveDictionary(unittest.TestCase):
    @unittest.skip
    def runTest(self):
        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'Barbara')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("gobble", [arg0, arg1])

        fake_verb_def = CDDefinition(EventType.INGEST)
        my_dict = {'gobble': fake_verb_def}

        def getitem(name):
            return my_dict[name]

        mock_dictionary = mock.MagicMock()
        mock_dictionary.__getitem__.side_effect = getitem
        # verbs.dictionary = mock_dictionary
        with patch('verbs.dictionary', new=mock_dictionary):

            prim_dict = {EventType.INGEST: fake_verb_def}

            def getprim(name):
                return prim_dict[name]

            mock_prim_dictionary = mock.MagicMock()
            mock_prim_dictionary.__getitem__.side_effect = getprim
            # primitives.dictionary = mock_prim_dictionary
            with patch('primitives.dictionary', new=mock_prim_dictionary):

                converter.convert_verb_event(mock_verb_data)

                mock_prim_dictionary.__getitem__.assert_any_call(EventType.INGEST)

class MergeFunctionWorks(unittest.TestCase):
    def runTest(self):
        from pymunk_cd.parsing.cd_converter import _merge_definitions

        def1 = CDDefinition(EventType.INGEST)
        def1.object_constraint = 'blah'
        def2 = CDDefinition()
        def2.sense_id = 'emit.01'
        def2.affected_attribute = EntityAttributes.VELOCITY
        def2.attribute_change_polarity = False


        result = _merge_definitions(def1, def2)

        self.assertEqual(result.primitive, EventType.INGEST)
        self.assertEqual(result.sense_id, 'emit.01')
        self.assertEqual(result.affected_attribute, EntityAttributes.VELOCITY)
        self.assertEqual(result.object_constraint, 'blah')
        self.assertEqual(result.attribute_change_polarity, False)
        


if __name__ == '__main__':
    unittest.main(module='cd_converter_tests')
