from unittest import mock
import unittest

import pymunk_cd.setup

from pymunk_cd.action_event import ActionEvent, EntityAttributes
from pymunk_cd.CDManager import CDManager
from pymunk_cd.primitives import Primitives

class SpawningEntities(unittest.TestCase):

    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)


    def test_adds_entity_for_single_item_event(self):

        fake_event = ActionEvent()
        fake_event.subject = 'Star'
        fake_event.affected_attribute = EntityAttributes.position
        
        pymunk_cd.setup._create_entities(self.manager, [fake_event])

        self.assertEqual(len(self.manager.objects), 1)

    def test_adds_entity_for_double_item_event(self):

        fake_event = ActionEvent()
        fake_event.subject = 'Star'
        fake_event.event_object ='particle'
        fake_event.affected_attribute = EntityAttributes.distance_from_subject
        
        pymunk_cd.setup._create_entities(self.manager, [fake_event])

        self.assertEqual(len(self.manager.objects), 2)

    def test_sets_velocity_for_ptrans_event(self):
        
        fake_event = ActionEvent()
        fake_event.subject = 'particle'
        fake_event.affected_attribute = EntityAttributes.position
        
        pymunk_cd.setup._create_entities(self.manager, [fake_event])

        particle = self.manager.objects[0].parts[0].body

        self.assertGreater(particle.velocity.get_length_sqrd(), 0)
