import random
import sys
from typing import List

import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import *

import condep.CompoundEntity as CompoundEntity
from condep import CDUtilities, utilities
from condep.action_event import (ActionEvent, EntityAttributeOutcomes,
                                    EntityAttributes)
from condep.cd_event import CDEvent
from condep.CDManager import CDManager
from condep.CDUtilities import CollisionTypes
from condep.definitions.primitives import dictionary as prim_definitions
from condep.parsing.cd_converter import CDConverter


def setup_pymunk_environment(events: List[ActionEvent], sentence: str=None):
    assert type(events) == list

    # pylint: disable=no-member
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption(sentence or 'Simulation')
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 0.0)

    space.add_collision_handler(
        CollisionTypes.ABSORBABLE, CollisionTypes.ABSORBER).begin = CDUtilities.CollisionAbsorber

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    manager = CDManager(screen, space)
    manager.print_events = False
    balls = []

    # Add objects
    _create_entities(manager, events)

    for entity in manager.objects:
        for particle in entity.parts:
            balls.append(particle)

    # Begin simulation
    while True:
        for keyboard_events in pygame.event.get():
            if keyboard_events.type == QUIT:
                sys.exit(0)
            elif keyboard_events.type == KEYDOWN and keyboard_events.key == K_ESCAPE:
                sys.exit(0)

        balls_to_remove = []
        for ball in balls:
            grav_force = pymunk.Vec2d()
            for other_ball in balls:
                grav_force = grav_force + \
                    utilities.calc_gravitational_force(
                        other_ball.body, ball.body)

            ball.body.apply_force_at_local_point(grav_force, (0, 0))

        for ball in balls_to_remove:
            space.remove(ball, ball.body)  # 3
            balls.remove(ball)  # 4

        steps_per_frame = 50  # larger value increases accuracy of simulation, but decreases speed
        frames_per_tick = 1

        for x in range(steps_per_frame):
            space.step(1/(frames_per_tick*steps_per_frame))

        screen.fill((255, 255, 255))

        space.debug_draw(draw_options)

        manager.tick()  # processes changes in CDobjects

        pygame.display.flip()
        # argument is max framerate, which we'll probably never reach!
        clock.tick(50)


#### PRIVATE METHODS ####
def _create_entities(manager: CDManager, events: List[ActionEvent]):
    event = events[0]

    # create entities
    subject_collision_type = None
    object_collision_type = None
    if (event.affected_attribute == EntityAttributes.inside_subject
            and event.attribute_outcome == EntityAttributeOutcomes.inside):
        subject_collision_type = CollisionTypes.ABSORBER
        object_collision_type = CollisionTypes.ABSORBABLE

    agent = _spawn_entity(manager, event.subject,
                          collision=subject_collision_type)

    if event.event_object:
        # work out relative starting position
        position_offset = 0
        if event.event_object:
            if event.affected_attribute == EntityAttributes.inside_subject:
                if event.attribute_outcome == EntityAttributeOutcomes.inside:
                    position_offset = -150
                else:
                    position_offset = 50

        patient = _spawn_entity(manager, event.event_object,
                                position_offset, collision=object_collision_type)
    else:
        patient = None

    _apply_attributes(event, agent, patient)
    for future_event in events[1:]:
        _queue_future_event(future_event, agent, patient)


def _spawn_entity(manager: CDManager, kind: str, offset: int=0, collision: CollisionTypes=None):
    '''Adds an entity of the specified kind to the space, with the optional 
    ability to set position and collision type'''

    x = 200 + offset
    y = 200 + offset

    kind = kind.lower()

    factory_dict = {
        'star': lambda manager: CDUtilities.create_big_particle(manager, x, y),
        'particle': lambda manager: CDUtilities.create_particle(manager, x, y, collision_type=collision),
        'radiation': lambda manager: CDUtilities.create_particle(manager, x, y, collision_type=collision),
    }

    return factory_dict[kind](manager)


def _apply_attributes(event: ActionEvent, agent: CompoundEntity, patient: CompoundEntity):
    '''Takes 'affected_attrbiute' info from ActionEvent and actually applies it to the entities'''

    attribute = event.affected_attribute
    assert attribute, 'Affected attribute should be set'

    if attribute == EntityAttributes.position or attribute == EntityAttributes.velocity:
        for part in agent.parts:
            part.body.velocity += 5
        agent.attribute_changes.append(
            [('event', event)]
            )

    elif attribute == EntityAttributes.inside_subject or attribute == EntityAttributes.distance_from_subject:
        for part in patient.parts:
            part.body.velocity += 8
        agent.attribute_changes.append(
            [('event', event)]
            )

    elif attribute == EntityAttributes.radius:
        part = agent.parts[0]
        target_radius = (0.5*part.radius
                         if event.attribute_outcome == EntityAttributeOutcomes.decrease
                         else 2*part.radius)
        agent.attribute_changes.append([('radius', target_radius)])

    elif attribute == None:
        pass

    else:
        raise NotImplementedError
        # TODO: fill in the rest

def _queue_future_event(event: ActionEvent, agent: CompoundEntity, patient: CompoundEntity):
    '''Takes 'affected_attrbiute' info from ActionEvent and actually applies it to the entities'''

    attribute = event.affected_attribute
    assert attribute, 'Affected attribute should be set'

    if attribute == EntityAttributes.position or attribute == EntityAttributes.velocity:
        for part in agent.parts:
            #part.body.velocity += 5
            raise NotImplementedError('queued velocity changes not yet done')

    elif attribute == EntityAttributes.inside_subject or attribute == EntityAttributes.distance_from_subject:
        for part in patient.parts:
            #part.body.velocity += 8
            raise NotImplementedError('queued velocity changes not yet done')

    elif attribute == EntityAttributes.radius:
        part = agent.parts[0]
        target_radius = (0.5*part.radius
                         if event.attribute_outcome == EntityAttributeOutcomes.decrease
                         else 2*part.radius)
        agent.attribute_changes.append([('radius', target_radius)])

    else:
        raise NotImplementedError
        # TODO: fill in the rest