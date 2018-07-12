import math
import pymunk
import pymunk_cd.CDEvent
import pymunk_cd.EventType as EventType
from pymunk_cd import *

class CompoundObject:
    def __init__(self, group=None):
        if(group == None):
            self.group = []
        else:
            self.group = group

        self.radius_history = []
        self.cog_history = []



    
    def tick(self):
        '''Updates history of properties and returns any events'''
        cog = self.get_centre_of_gravity()
        self.cog_history.append(cog)

        self.radius_history.append(self.get_max_radius(cog))

        #check for events
        min_event_span = 5

        #check radius
        if(len(self.radius_history) < min_event_span):
            return False

        first_index = len(self.radius_history) - min_event_span
        

        for i, j in zip(self.radius_history, self.radius_history[first_index:]):
            if(j > i):
                return []
            
        return pymunk_cd.CDEvent.CDEvent(self, EventType.EventType.MOVE)


    # Get methods
    def get_max_radius(self, cog = None):
        centre_of_gravity = cog or self.get_centre_of_gravity()
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
