import pymunk

def to_pygame(p:int):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)


def calc_gravitational_force(body1:pymunk.Body, body2:pymunk.Body):
    G = 1000
    translation_vec = (body1.position - body2.position)
    r_sqrd = translation_vec.get_length_sqrd()
    if(r_sqrd == 0):
        return pymunk.Vec2d()

    force_vector = (G*body1.mass*body2.mass)*translation_vec/r_sqrd
    
    return force_vector

def warn(message:str):
    '''Prints a warning in yellow text'''
    print('\033[93m' + message + '\033[0m') 