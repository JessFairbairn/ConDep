from unittest import mock
import unittest

import condep.setup

from condep.action_event import ActionEvent, EntityAttributes, EntityAttributeOutcomes
from condep.CDManager import CDManager
from condep.primitives import Primitives
from condep.CompoundEntity import CompoundEntity

class SpawningEntities(unittest.TestCase):

    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)


    def test_adds_entity_for_single_item_event(self):

        fake_event = ActionEvent()
        fake_event.subject = 'Star'
        fake_event.affected_attribute = EntityAttributes.position
        
        condep.setup._create_entities(self.manager, [fake_event])

        self.assertEqual(len(self.manager.objects), 1)

    def test_adds_entity_for_double_item_event(self):

        fake_event = ActionEvent()
        fake_event.subject = 'Star'
        fake_event.event_object ='particle'
        fake_event.affected_attribute = EntityAttributes.distance_from_subject
        
        condep.setup._create_entities(self.manager, [fake_event])

        self.assertEqual(len(self.manager.objects), 2)

    def test_sets_velocity_for_ptrans_event(self):
        
        fake_event = ActionEvent()
        fake_event.subject = 'particle'
        fake_event.affected_attribute = EntityAttributes.position
        
        condep.setup._create_entities(self.manager, [fake_event])

        particle = self.manager.objects[0].parts[0].body

        self.assertGreater(particle.velocity.get_length_sqrd(), 0)

class ApplyAttributes(unittest.TestCase):
    def test_adds_attribute_change_for_inside_subject_event(self):
        event = ActionEvent()
        event.affected_attribute = EntityAttributes.inside_subject
        event.attribute_outcome = EntityAttributeOutcomes.inside

        agent = CompoundEntity()
        patient = CompoundEntity()

        condep.setup._apply_attributes(event, agent, patient)


        self.assertIn(('event',event), agent.attribute_changes[0])

    def test_adds_attribute_change_for_distance_from_subject_event(self):
        event = ActionEvent()
        event.affected_attribute = EntityAttributes.distance_from_subject
        event.attribute_outcome = EntityAttributeOutcomes.increase

        agent = CompoundEntity()
        patient = CompoundEntity()

        condep.setup._apply_attributes(event, agent, patient)


        self.assertIn(('event',event), agent.attribute_changes[0])