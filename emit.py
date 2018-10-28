#!/usr/bin/env python3

import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import condep.CompoundEntity
import condep.CDManager

from condep import utilities

from condep import CDUtilities    

def main():
    #pylint: disable=no-member
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Emit")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 0.0)

    
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    manager = condep.CDManager.CDManager(screen,space)
    star = CDUtilities.create_spitting_star(manager)
    balls = star.parts

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
        

if __name__ == '__main__':
    main()