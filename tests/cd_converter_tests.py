from unittest import mock
from unittest.mock import patch
import unittest

from pymunk_cd.action_event import ActionEvent
from pymunk_cd.action_event import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.primitives import Primitives

from pymunk_cd.parsing import cd_converter
from pymunk_cd.parsing.NLPParser import NLPParser
from pymunk_cd.parsing.VerbSense import VerbArgumentInstance
from pymunk_cd.parsing.VerbSense import VerbSense
from pymunk_cd.parsing.cd_definitions import CDDefinition, CDDefinitionPredecessorWrapper

from pymunk_cd.definitions import verbs
from pymunk_cd.definitions import primitives


class ConvertVerbToCdEvent(unittest.TestCase):
    def test_ReturnsCorrectSubjectAndObject(self):

        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("emit", [arg0, arg1])

        result = converter.convert_verb_event_to_cd_event(mock_verb_data)

        self.assertEqual(result.subject, arg0.argument,
                         'should set the correct subject for the cd event')
        self.assertEqual(result.event_object, arg1.argument,
                         'should set the correct object for the cd event')

    #@unittest.skip
    def test_CallsVerbDictionary(self):
        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'black hole')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("spew", [arg0, arg1])

        my_dict = {'spew': CDDefinition(Primitives.EXPEL)}

        def getitem(name):
            return my_dict[name]

        mock_dictionary = mock.MagicMock()
        mock_dictionary.__getitem__.side_effect = getitem
        with patch('pymunk_cd.definitions.verbs.dictionary', new=mock_dictionary):

            converter.convert_verb_event_to_cd_event(mock_verb_data)

            mock_dictionary.__getitem__.assert_any_call('spew')

    #@unittest.skip
    def test_CallsPrimitiveDictionary(self):

        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'Barbara')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("gobble", [arg0, arg1])

        fake_verb_def = CDDefinition(Primitives.INGEST)
        fake_verb_def.sense_id = 'gobble'
        my_dict = {'gobble': fake_verb_def}

        def getitem(name):
            return my_dict[name]

        mock_dictionary = mock.MagicMock()
        mock_dictionary.__getitem__.side_effect = getitem
        
        with patch('pymunk_cd.definitions.verbs.dictionary', new=mock_dictionary):

            prim_dict = {Primitives.INGEST: fake_verb_def}

            def getprim(name):
                return prim_dict[name]

            mock_prim_dictionary = mock.MagicMock()
            mock_prim_dictionary.__getitem__.side_effect = getprim
            
            with patch('pymunk_cd.definitions.primitives.dictionary', new=mock_prim_dictionary):

                converter.convert_verb_event_to_cd_event(mock_verb_data)

                mock_prim_dictionary.__getitem__.assert_any_call(
                    Primitives.INGEST)

    def test_SetsPrecedingEvents(self):

        converter = cd_converter.CDConverter()

        arg0 = VerbArgumentInstance('emitting entity', 'PAG', 'Barbara')
        arg1 = VerbArgumentInstance('thing emitted', 'PPT', 'radiation')
        mock_verb_data = VerbSense("nom", [arg0, arg1])

        fake_verb_def = CDDefinition(Primitives.INGEST)
        fake_verb_def.sense_id = 'nom'
        fake_verb_def.preceding = CDDefinitionPredecessorWrapper()

        pred_def = CDDefinition(Primitives.PROPEL)
        fake_verb_def.preceding.definition = pred_def


        my_dict = {'nom': fake_verb_def}

        def getitem(name):
            return my_dict[name]

        mock_dictionary = mock.MagicMock()
        mock_dictionary.__getitem__.side_effect = getitem
        
        with patch('pymunk_cd.definitions.verbs.dictionary', new = mock_dictionary):

            event = converter.convert_verb_event_to_cd_event(mock_verb_data)
            self.assertEqual(event.preceding.primitive, Primitives.PROPEL)

                


class ConvertCDEventToActionEvent(unittest.TestCase):
    def test_returns_action_event(self):
        converter = cd_converter.CDConverter()

        fake_cd_event = CDEvent(Primitives.EXPEL)

        result = converter.convert_cd_event_to_action_events(fake_cd_event)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], ActionEvent)

    def test_sets_attributes_correctly(self):
        converter = cd_converter.CDConverter()

        fake_cd_event = CDEvent(Primitives.EXPEL)

        result = converter.convert_cd_event_to_action_events(fake_cd_event)
        self.assertEqual(result[0].affected_attribute, EntityAttributes.inside_subject)
        self.assertEqual(result[0].attribute_outcome, EntityAttributeOutcomes.outside)

    def test_sets_subject_and_object_correctly(self):
        converter = cd_converter.CDConverter()

        fake_cd_event = CDEvent(Primitives.EXPEL)
        fake_cd_event.subject = "Star"
        fake_cd_event.event_object = "particle"

        result = converter.convert_cd_event_to_action_events(fake_cd_event)
        self.assertEqual(result[0].subject, "Star")
        self.assertEqual(result[0].event_object, "particle")

    def test_sets_order_of_action_events_correctly(self):
        converter = cd_converter.CDConverter()

        cd_event_1 = CDEvent(Primitives.EXPEL)
        cd_event_2 = CDEvent(Primitives.PTRANS)
        cd_event_3 = CDEvent(Primitives.INGEST)

        cd_event_1.preceding = cd_event_2
        cd_event_2.preceding = cd_event_3

        results = converter.convert_cd_event_to_action_events(cd_event_1)
        self.assertEqual(len(results), 3, 'Should return 3 action events from nested CD input')

        self.assertEqual(results[0].affected_attribute, EntityAttributes.inside_subject)
        self.assertEqual(results[0].attribute_outcome, EntityAttributeOutcomes.inside)

        self.assertEqual(results[1].affected_attribute, EntityAttributes.position)

        self.assertEqual(results[2].affected_attribute, EntityAttributes.inside_subject)
        self.assertEqual(results[2].attribute_outcome, EntityAttributeOutcomes.outside)
        

if __name__ == '__main__':
    unittest.main(module='cd_converter_tests')
