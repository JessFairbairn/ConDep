import sys, random, enum
import pygame
import pymunk

from .CDManager import CDManager
from .CompoundEntity import CompoundEntity

class CollisionTypes:
    ABSORBABLE = 1
    ABSORBER = 2

def add_ball(space, x:int, y:int, collision_type:int=None, radius=4, mass=1):
        
    moment = pymunk.moment_for_circle(mass, 0, radius) # 1
    body = pymunk.Body(mass, moment) # 2
    body.position = x, y # 3
    
    shape = pymunk.Circle(body, radius) # 4
    
    if collision_type:
        shape.collision_type = collision_type
        if collision_type == CollisionTypes.ABSORBABLE:
            shape.elasticity = 1
    space.add(body, shape) # 5
    return shape

def create_big_particle(manager, x_loc:int=300, y_loc:int=300):
    'Creates a plain star, adds it to CD manager, pymunk and pygame'

    # setup CD stuff
    star = CompoundEntity()
    star.name = 'Star1'

    manager.objects.append(star)
    
    x = x_loc
    y = y_loc
    ball_shape = add_ball(manager.space, x, y, radius=40, mass=40, collision_type=CollisionTypes.ABSORBER)
    
    star.parts.append(ball_shape)

    return star

def create_star(manager, x_loc:int=300, y_loc:int=300, num_particles = None):
    'Creates a plain star, adds it to CD manager, pymunk and pygame'
    num_particles = num_particles or 40

    # setup CD stuff
    star = CompoundEntity()
    star.name = 'Star1'

    manager.objects.append(star)

    for n in range(num_particles):
        x = random.randint(x_loc-100, x_loc+100)
        y = random.randint(y_loc - 100, y_loc + 100)
        ball_shape = add_ball(manager.space, x, y)
        star.parts.append(ball_shape)

    return star

def create_spitting_star(manager:CDManager, num_particles = None):
    'Creates a star which spits out some of it\'s parts, adds it to CD manager, pymunk and pygame'
    num_particles = num_particles or 40

    # setup CD stuff
    star = CompoundEntity()
    star.name = 'Star1'

    manager.objects.append(star)

    for n in range(num_particles):
        x = random.randint(200, 400)
        y = random.randint(200, 400)
        ball_shape = add_ball(manager.space, x, y)
        star.parts.append(ball_shape)

    ball_with_momentum = add_ball(manager.space, 300,300)
    star.parts.append(ball_with_momentum)
    ball_with_momentum.body.velocity = pymunk.Vec2d(80,0)


    return star

def create_particle(manager:CDManager, x:int, y:int, collision_type:CollisionTypes=None):
    'Creates a plain star, adds it to CD manager, pymunk and pygame'

    # setup CD stuff
    particle = CompoundEntity()
    particle.name = 'Particle'

    manager.objects.append(particle)
    
    ball_shape = add_ball(manager.space, x, y, collision_type=collision_type)
    particle.parts.append(ball_shape)

    return particle

def CollisionAbsorber(arbiter, space, data):
    absorber = arbiter.shapes[0]
    absorbable = arbiter.shapes[1]

    
    joint = pymunk.SlideJoint(absorber.body, absorbable.body, (0,0), (0,0), 0, 40)
    
    space.add(joint)
    
    # absorbable.body.velocity = pymunk.Vec2d()
    
    absorbable.sensor = True
    return True