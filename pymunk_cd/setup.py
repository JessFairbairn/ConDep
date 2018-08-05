import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import pymunk_cd.CompoundEntity
from pymunk_cd.cd_event import CDEvent
from pymunk_cd.CDManager import CDManager

from pymunk_cd import utilities

from pymunk_cd import CDUtilities

def setup_pymunk_environment(event:CDEvent):
    #pylint: disable=no-member
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Emit")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 0.0)

    
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    manager = pymunk_cd.CDManager.CDManager(screen,space)
    
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

def create_entities(manager:CDManager, event:CDEvent):
    spawn_entity(manager, event.subject)

    if event.event_object:
        spawn_entity(manager, event.event_object)


def spawn_entity(manager:CDManager, kind:str):
    kind = kind.lower()

    factory_dict = {
        'star' : lambda manager: CDUtilities.create_star(manager),
        'particle': lambda manager: CDUtilities.create_particle(manager, 1, 1),
    }

    factory_dict[kind](manager)