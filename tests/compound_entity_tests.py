from unittest import mock
from unittest.mock import patch
import unittest

from pymunk.vec2d import Vec2d

from pymunk_cd.action_event import ActionEvent
from pymunk_cd.action_event import EntityAttributes
from pymunk_cd.action_event import EntityAttributeOutcomes
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.CDManager import CDManager
from pymunk_cd.primitives import Primitives
import pymunk_cd.CDUtilities as CDUtilities

from pymunk_cd.CompoundEntity import CompoundEntity


class UpdateChangingAttributes(unittest.TestCase):

    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)

    def test_handles_queued_radius_increase(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        
        original_radius = entity.parts[0].radius
        entity.attribute_changes = [[('radius', original_radius*2)]]

        # act
        entity._update_changing_attributes()

        # assert
        self.assertGreater(entity.parts[0].radius, original_radius, 'Should increase the radius')

    def test_handles_queued_event_target(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        
        target_event = ActionEvent()
        actual_event = ActionEvent()

        entity.event_history.append([actual_event])
        entity.attribute_changes = [[('event', target_event)]]

        # act
        entity._update_changing_attributes()

        # assert
        self.assertEqual(len(entity.attribute_changes), 0, 'Should have no more queued changes')

    def test_removes_fulfilled_targets(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        
        original_radius = entity.parts[0].radius
        entity.attribute_changes = [
            [('radius', original_radius), ('position', 999)]
            ]
        self.assertEqual(len(entity.attribute_changes[0]), 2, 'Checking arrangement!')

        # act
        entity._update_changing_attributes()

        # assert
        self.assertEqual(len(entity.attribute_changes[0]), 1, 'Should be only have one left')
        self.assertTupleEqual(entity.attribute_changes[0][0], ('position', 999),
            'Should have left unfulfilled target')

    def test_removes_fulfilled_group_of_targets(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        
        original_radius = entity.parts[0].radius
        entity.attribute_changes = [
            [('radius', original_radius)],
            [('future_target', 42)]
            ]

        # act
        entity._update_changing_attributes()

        # assert
        self.assertEqual(len(entity.attribute_changes), 1, 'Should remove empty group of targets')
        self.assertTupleEqual(entity.attribute_changes[0][0], ('future_target', 42),
            'Should future target should have moved into first position')

    def test_handles_empty_list_without_freaking_out(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        
        entity.attribute_changes = []

        # act
        entity._update_changing_attributes()

    def test_handles_compound_entities(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        new_particle = CDUtilities.add_ball(self.manager.space, 11, 11)
        entity.parts.append(new_particle)
        
        target_event = ActionEvent()
        actual_event = ActionEvent()

        entity.event_history.append([actual_event])
        entity.attribute_changes = [[('event', target_event)]]

        # act
        entity._update_changing_attributes()

        # assert
        self.assertEqual(len(entity.attribute_changes), 0)

class CheckForEvents(unittest.TestCase):
    def test_returns_empty_list_when_no_changes_but_above_min_length(self):
        entity = CompoundEntity()
        entity.radius_history = [1000,1000,1000,1000,1000]
        entity.cog_history = [Vec2d(),Vec2d(),Vec2d(),Vec2d(),Vec2d()]
        entity.cog_delta_history = [0, 0, 0, 0, 0]

        found_events = entity._check_for_events()

        self.assertIsInstance(found_events, list)
        self.assertListEqual(found_events,[])

class GetInclusionRadius(unittest.TestCase):
    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)

    def test_handles_single_particle(self):
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        output = entity.get_inclusion_radius()

        self.assertEqual(output, 40)

    def test_handles_multiple_particles(self):
        entity = CDUtilities.create_star(self.manager, 10, 10)
        entity.get_inclusion_radius()

    def test_at_least_radius_of_biggest_particle(self):
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        new_particle = CDUtilities.add_ball(self.manager.space, 11, 11)
        entity.parts.append(new_particle)

        output = entity.get_inclusion_radius()

        self.assertEqual(output, 40)


class GetCentreOfGravity(unittest.TestCase):
    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)

    def test_correct_for_large_particles(self):
        entity = CDUtilities.create_big_particle(self.manager, 10, 10)
        body = entity.parts[0].body
        
        self.assertEqual(entity.get_centre_of_gravity(), body.position)

class CheckForEmitOrInject(unittest.TestCase):
    @mock.patch('pygame.surface.Surface')
    @mock.patch('pymunk.Space')
    def setUp(self, mockSurface, mockSpace):
        self.manager = CDManager(mockSurface, mockSpace)

    def test_recognises_expell_for_compound_entity(self):
        entity = CDUtilities.create_star(self.manager,0,0)
        entity.parts[0].body.position = Vec2d(200,200)
        entity.parts[0].mark = 'Outlier'
        self.manager.distance_matrices = [
            [[None]]
        ]

        events = entity._check_for_injest_or_emit(self.manager, Vec2d(0,0))

        self.assertGreater(len(events), 0, 'Should return an event')
        event = events[0]
        self.assertEqual(event.affected_attribute, EntityAttributes.inside_subject)
        self.assertEqual(event.attribute_outcome, EntityAttributeOutcomes.outside)
        self.assertEqual(event.event_object.mark, 'Outlier')


    def test_recognises_absorb_for_simple_entity(self):
        # arrange
        entity = CDUtilities.create_big_particle(self.manager,0,0)
        particle = CDUtilities.create_particle(self.manager,1,1)
        self.manager.distance_matrices = [[
            [None, 20], 
            [20, None]
            ]]

        # act
        events = entity._check_for_injest_or_emit(self.manager, Vec2d(0,0))

        # assert
        self.assertEqual(len(events), 1, 'Should return a single event')
        event = events[0]
        self.assertEqual(event.affected_attribute, EntityAttributes.inside_subject)
        self.assertEqual(event.attribute_outcome, EntityAttributeOutcomes.inside)
        # self.assertEqual(event.event_object.mark, 'Outlier')

if __name__ == '__main__':
    unittest.main()
