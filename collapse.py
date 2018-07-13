#!/usr/bin/env python3

import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

import pymunk_cd.CompoundObject
import pymunk_cd.CDManager

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)

def add_ball(space):
    mass = 1
    radius = 4
    moment = pymunk.moment_for_circle(mass, 0, radius) # 1
    body = pymunk.Body(mass, moment) # 2cog
    x = random.randint(200, 400)
    y = random.randint(200, 400)
    body.position = x, y # 3
    shape = pymunk.Circle(body, radius) # 4
    space.add(body, shape) # 5
    return shape

def calc_gravitational_force(body1,body2):
    G = 500
    translation_vec = (body1.position - body2.position)
    r_sqrd = translation_vec.get_length_sqrd()
    if(r_sqrd == 0):
        return pymunk.Vec2d()

    force_vector = (G*body1.mass*body2.mass)*translation_vec/r_sqrd
    
    return force_vector

    

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Collapse")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 0.0)

    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    NUM_BALLS = 40

    # setup CD stuff
    star = pymunk_cd.CompoundObject.CompoundObject()
    star.name = 'Star1'

    manager = pymunk_cd.CDManager.CDManager(screen)
    manager.objects.append(star)

    for n in range(NUM_BALLS):
        ball_shape = add_ball(space)
        balls.append(ball_shape)
        star.group.append(ball_shape)

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
                grav_force = grav_force + calc_gravitational_force(other_ball.body, ball.body)

            ball.body.apply_force_at_local_point(grav_force, (0,0))

        for ball in balls_to_remove:
            space.remove(ball, ball.body) # 3
            balls.remove(ball) # 4

        steps_per_frame = 50 #larger value increases accuracy of simulation, but decreases speed
        frames_per_tick = 1

        for x in range(steps_per_frame):
            space.step(1/(frames_per_tick*steps_per_frame))

        screen.fill((255,255,255))

        pygame.draw.circle(screen, 
            (0,0,0),
            to_pygame(star.get_centre_of_gravity()),
            int(star.get_max_radius()),
            1
        )
        space.debug_draw(draw_options)


        manager.tick() #processes changes in CDobjects

        pygame.display.flip()
        clock.tick(50) # argument is max framerate, which we'll probably never reach!

        

if __name__ == '__main__':
    main()