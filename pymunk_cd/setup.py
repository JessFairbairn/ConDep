import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import pymunk_cd.CompoundEntity
from pymunk_cd.action_event import EntityAttributes, EntityAttributeOutcomes
from pymunk_cd.action_event import ActionEvent
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.CDManager import CDManager
from pymunk_cd.CDUtilities import CollisionTypes

from pymunk_cd.definitions.primitives import dictionary as prim_definitions

from pymunk_cd.parsing.cd_converter import CDConverter

from pymunk_cd import utilities

from pymunk_cd import CDUtilities

def setup_pymunk_environment(event:ActionEvent, sentence:str=None):
    assert type(event) == ActionEvent

    #pylint: disable=no-member
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption(sentence or 'Simulation')
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 0.0)

    space.add_collision_handler(CollisionTypes.ABSORBABLE, CollisionTypes.ABSORBER).begin = CDUtilities.CollisionAbsorber
    
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    manager = pymunk_cd.CDManager.CDManager(screen,space)
    manager.print_events = False
    balls = []

    # Add objects
    create_entities(manager, event)

    for entity in manager.objects:
        for particle in entity.parts:
            balls.append(particle)

    # Begin simulation
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        balls_to_remove = []
        for ball in balls:
            grav_force = pymunk.Vec2d()
            for other_ball in balls:
                grav_force = grav_force + utilities.calc_gravitational_force(other_ball.body, ball.body)

            ball.body.apply_force_at_local_point(grav_force, (0,0))

        for ball in balls_to_remove:
            space.remove(ball, ball.body) # 3
            balls.remove(ball) # 4

        steps_per_frame = 50 #larger value increases accuracy of simulation, but decreases speed
        frames_per_tick = 1

        for x in range(steps_per_frame):
            space.step(1/(frames_per_tick*steps_per_frame))

        screen.fill((255,255,255))

        space.debug_draw(draw_options)

        manager.tick() #processes changes in CDobjects

        pygame.display.flip()
        clock.tick(50) # argument is max framerate, which we'll probably never reach!

def create_entities(manager:CDManager, event:ActionEvent):
    

    #create entities
    agent = spawn_entity(manager, event.subject)

    if event.event_object:
        #work out relative starting position
        position_offset = 0
        if event.event_object:
            if event.affected_attribute == EntityAttributes.inside_subject:
                if event.attribute_outcome == EntityAttributeOutcomes.inside:
                    position_offset = -150
                else:
                    position_offset = 50

        patient = spawn_entity(manager, event.event_object, position_offset)

    attribute = event.affected_attribute

    if attribute == EntityAttributes.position or attribute == EntityAttributes.velocity:
        for part in agent.parts:
            part.body.velocity += 5
    elif attribute == EntityAttributes.inside_subject or attribute == EntityAttributes.distance_from_subject:
        for part in patient.parts:
            part.body.velocity += 8
    elif attribute == EntityAttributes.radius:
        part = agent.parts[0]
        target_radius = (0.5*agent.radius 
            if event.attribute_outcome == EntityAttributeOutcomes.decrease
            else 2*part.radius)
        agent.attribute_changes.append(('radius',target_radius))
    else:
        raise NotImplementedError
        #TODO: fill in the rest


def spawn_entity(manager:CDManager, kind:str, offset:int=0):

    
    x = 200 + offset
    y = 200 + offset    

    kind = kind.lower()

    factory_dict = {
        'star' : lambda manager: CDUtilities.create_big_particle(manager, x, y),
        'particle': lambda manager: CDUtilities.create_particle(manager, x, y),
    }

    return factory_dict[kind](manager)