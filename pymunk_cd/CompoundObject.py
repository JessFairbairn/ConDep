import math
import pymunk

class CompoundObject:
    def __init__(self, group=None):
        if(group == None):
            self.group = []
        else:
            self.group = group

    def get_max_radius(self):
        centre_of_gravity = self.get_centre_of_gravity()
        max_r_sqrd = 0
        for shape1 in self.group:            
            translation_vec = (shape1.body.position - centre_of_gravity)
            r_sqrd = translation_vec.get_length_sqrd()
            if(r_sqrd > max_r_sqrd):
                max_r_sqrd = r_sqrd
        return math.sqrt(max_r_sqrd)

    def get_centre_of_gravity(self):
        weighted_vector_sum = pymunk.Vec2d()
        for shape in self.group:
            body = shape.body
            weighted_vector_sum = weighted_vector_sum + body.mass * body.position
        
        return weighted_vector_sum/len(self.group)