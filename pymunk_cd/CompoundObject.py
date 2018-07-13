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

        self.name = None


    
    def tick(self):
        "Updates history of properties and returns any events"
        cog = self.get_centre_of_gravity()
        self.cog_history.append(cog)

        self.radius_history.append(self.get_max_radius(cog))

        #check for events
        min_event_span = 4
        if(len(self.radius_history) < min_event_span):
            return []
        
        first_index = len(self.radius_history) - min_event_span

        #check for whole object movements
        recent_cog_history = self.cog_history[first_index:]
        x_coords = list(map(lambda cog: cog.x, recent_cog_history))
        y_coords = list(map(lambda cog: cog.y, recent_cog_history))
        if (max(x_coords) - min(x_coords) > 5) or (max(y_coords) - min(y_coords) > 5):
            return [pymunk_cd.CDEvent.CDEvent(self, EventType.EventType.PTRANS)]

        #check radius
        for i, j in zip(self.radius_history[first_index-1:], self.radius_history[first_index:]):
            if(j > i):
                return []

        new_event = pymunk_cd.CDEvent.CDEvent(self, EventType.EventType.MOVE)
        new_event.part = "radius"
        new_event.direction = "decrease"
        return [new_event]


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
