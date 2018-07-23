import math
import pymunk
from .action_event import ActionEvent
from .action_event import EntityAttributes
import pymunk_cd.EventType as EventType
# from .EventType import EventType
from pymunk_cd import *

import statistics

class CompoundEntity:
    def __init__(self, parts=None):
        if(parts == None):
            self.parts = []
        else:
            self.parts = parts

        self.radius_history = []
        self.cog_history = []

        self.name = None

    
    def tick(self):
        "Updates history of properties and returns any events"
        
        cog = self.get_centre_of_gravity()
        inclusion_radius = self.get_inclusion_radius(cog)
        distances_from_centre = self.get_distances_from_cog(cog)

        new_events = []

        # check for parts of the object seperating/leaving
        has_exited = list(map(lambda part_dist: part_dist > inclusion_radius, distances_from_centre))        
        
        for idx in range(len(has_exited) - 1, 0, -1):
            if has_exited[idx]:
                #remove from parts
                removed_object = self.parts[idx]
                del self.parts[idx]
                emit_event = ActionEvent()
                emit_event.event_object = removed_object
                emit_event.subject = self
                emit_event.affected_attribute = EntityAttributes.inside_subject
                emit_event.attribute_change_polarity = False
                new_events.append(emit_event)

        

        #Then log to histories
        cog = self.get_centre_of_gravity()
        self.cog_history.append(cog)
        self.radius_history.append(self.get_max_radius(cog))

        #check for events
        min_event_span = 4
        if(len(self.radius_history) < min_event_span):
            return new_events
        
        first_index = len(self.radius_history) - min_event_span

        #check for whole object movements
        recent_cog_history = self.cog_history[first_index:]
        x_coords = list(map(lambda cog: cog.x, recent_cog_history))
        y_coords = list(map(lambda cog: cog.y, recent_cog_history))

        if (max(x_coords) - min(x_coords) > 5) or (max(y_coords) - min(y_coords) > 5):
            event = ActionEvent()
            event.affected_attribute = EntityAttributes.position #something to better express this
            event.subject = self

            new_events.append(event)
            return new_events

        #check radius
        for i, j in zip(self.radius_history[first_index-1:], self.radius_history[first_index:]):
            if(j > i):
                return new_events

        radius_change = ActionEvent()
        radius_change.subject = self
        radius_change.affected_attribute = EntityAttributes.radius
        radius_change.attribute_change_polarity = True
        new_events.append(radius_change)
        return new_events


    # Get methods

    def get_distances_from_cog(self, cog = None):
        'Returns the distance of each particle from the centre of gravity'

        centre_of_gravity = cog or self.get_centre_of_gravity()

        return list(
                map(lambda part: (part.body.position - centre_of_gravity).get_length(), self.parts)
            )


    def get_inclusion_radius(self, cog = None):
        'Returns the mean radius plus 2 standard deviations'

        distances_from_cog = self.get_distances_from_cog(cog)
        
        mean_distance = statistics.mean(distances_from_cog)
        sd =  statistics.stdev(distances_from_cog, mean_distance)
        return mean_distance + 2*sd


    def get_max_radius(self, cog = None):
        centre_of_gravity = cog or self.get_centre_of_gravity()
        max_r_sqrd = 0
        for shape1 in self.parts:            
            translation_vec = (shape1.body.position - centre_of_gravity)
            r_sqrd = translation_vec.get_length_sqrd()
            if(r_sqrd > max_r_sqrd):
                max_r_sqrd = r_sqrd
        return math.sqrt(max_r_sqrd)

    def get_centre_of_gravity(self):
        weighted_vector_sum = pymunk.Vec2d()
        for shape in self.parts:
            body = shape.body
            weighted_vector_sum = weighted_vector_sum + body.mass * body.position
        
        return weighted_vector_sum/len(self.parts)
