import math
import pymunk
from .action_event import ActionEvent
from .action_event import EntityAttributes
from .action_event import EntityAttributeOutcomes
import condep.primitives as EventType
# from .EventType import EventType
from condep import *

import statistics


class CompoundEntity:
    def __init__(self, parts:list = None):
        if(parts == None):
            self.parts = []
        else:
            self.parts = parts

        self.radius_history = []
        self.cog_history = []
        self.cog_delta_history = []

        self.attribute_changes = []

        self.event_history = []

        self.name = None  # Type: str

    def __str__(self):
        return self.name

    def tick(self, manager):
        "Updates history of properties and returns any events"

        cog = self.get_centre_of_gravity()

        new_events = []

        # Check for particles joining or leaving
        new_events.extend(self._check_for_injest_or_emit(manager, cog))

        # Update changing attributes
        self._update_changing_attributes()

        # Then log to histories
        cog = self.get_centre_of_gravity()
        self.cog_history.append(cog)

        history_length = len(self.cog_history)
        if history_length > 1:
            cog_delta = self.cog_history[history_length -
                                         1] - self.cog_history[history_length - 2]
            self.cog_delta_history.append(cog_delta.get_length())

        self.radius_history.append(self.get_max_radius(cog))

        # CHECK FOR EVENTS
        new_events.extend(self._check_for_events())

        self.event_history.append(new_events)

        return new_events

    

    ### Get methods ###
    def get_distances_from_cog(self, cog=None):
        'Returns the distance of each particle from the centre of gravity'

        centre_of_gravity = cog or self.get_centre_of_gravity()

        return list(
            map(lambda part: (part.body.position -
                              centre_of_gravity).get_length(), self.parts)
        )

    def get_inclusion_radius(self, cog=None):
        'Returns the mean radius plus 2 standard deviations'
        if len(self.parts) == 1:
            return self.parts[0].radius

        biggest_particle_radius = max(map(lambda particle: particle.radius, self.parts))

        distances_from_cog = self.get_distances_from_cog(cog)

        if max(distances_from_cog) < biggest_particle_radius:
            return biggest_particle_radius

        mean_distance = statistics.mean(distances_from_cog)
        sd = statistics.stdev(distances_from_cog, mean_distance)
        return mean_distance + 2*sd

    def get_max_radius(self, cog=None):
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
        total_mass = 0
        for shape in self.parts:
            body = shape.body
            total_mass += body.mass
            weighted_vector_sum = weighted_vector_sum + body.mass * body.position

        return weighted_vector_sum/total_mass

    #### Private Methods ####
    def _check_for_injest_or_emit(self, manager, cog:pymunk.Vec2d):
        new_events = []
        inclusion_radius = self.get_inclusion_radius(cog)

        # Check for expel events
        if len(self.parts) > 1:
            # check for parts of the object seperating/leaving
            distances_from_centre = self.get_distances_from_cog(cog)

            has_exited = list(map(lambda part_dist: part_dist >
                                  inclusion_radius, distances_from_centre))

            for idx in range(len(has_exited) - 1, -1, -1):
                if has_exited[idx]:
                    # remove from parts
                    removed_object = self.parts[idx]
                    del self.parts[idx]

                    # add event
                    emit_event = ActionEvent()
                    emit_event.event_object = removed_object
                    emit_event.subject = self
                    emit_event.affected_attribute = EntityAttributes.inside_subject
                    emit_event.attribute_outcome = EntityAttributeOutcomes.outside
                    new_events.append(emit_event)

                    # TODO: create a compound object for newly seperate obj

        # Check for ingest events
        distance_matrix = manager.distance_matrices[-1]
        entity_index = manager.get_entity_index(self)

        distances_from_entity = distance_matrix[entity_index]

        for idx in range(len(distances_from_entity) - 1, -1, -1):
            if distances_from_entity[idx] and distances_from_entity[idx] < inclusion_radius:
                swallowed_entity = manager.objects[idx]

                # add to parts
                self.parts.extend(swallowed_entity.parts)

                # add event
                injest_event = ActionEvent()
                injest_event.event_object = swallowed_entity
                injest_event.subject = self
                injest_event.affected_attribute = EntityAttributes.inside_subject
                injest_event.attribute_outcome = EntityAttributeOutcomes.inside
                new_events.append(injest_event)

                # remove swallowed object from manager
                manager.objects[idx]= None

                

        return new_events

    def _check_for_events(self):
        min_event_span = 4
        new_events = []

        if len(self.radius_history) < min_event_span:
            return new_events

        first_index = len(self.radius_history) - min_event_span

        # check for whole object movements
        recent_cog_history = self.cog_history[first_index:]
        x_coords = list(map(lambda cog: cog.x, recent_cog_history))
        y_coords = list(map(lambda cog: cog.y, recent_cog_history))

        min_movement = 5
        if (max(x_coords) - min(x_coords) > min_movement) or (max(y_coords) - min(y_coords) > min_movement):
            event = ActionEvent()
            event.affected_attribute = EntityAttributes.position
            event.subject = self

            new_events.append(event)
            return new_events

        recent_delta_history = self.cog_delta_history[first_index:]

        if (max(recent_delta_history) - min(recent_delta_history)) > 0.5:
            event = ActionEvent()
            event.affected_attribute = EntityAttributes.velocity
            event.subject = self
            # TODO: add increase/decrease outcome
            new_events.append(event)

        # check distances from other objects
        # index = manager.get_entity_index(self)
        # manager.distance_matrices
        # TODO: implement this

        # check radius
        if len(self.parts) > 1:
            radius_changes = list(
                zip(self.radius_history[first_index-1:], self.radius_history[first_index:]))
            is_increase = radius_changes[0][1] > radius_changes[0][0]
            for i, j in radius_changes:
                if (j > i) != is_increase:  # check the direction of radius change is consistent over 5 ticks
                    return new_events

            radius_change = ActionEvent()
            radius_change.subject = self
            radius_change.affected_attribute = EntityAttributes.radius
            radius_change.attribute_outcome = (
                EntityAttributeOutcomes.increase if is_increase else EntityAttributeOutcomes.decrease
            )
            new_events.append(radius_change)

        return new_events

    def _update_changing_attributes(self):
        if self.attribute_changes:

            for target in self.attribute_changes[0]:
                if target[0] == 'event':
                    try:
                        recent_events = self.event_history[-1]
                    except IndexError:
                        continue

                    target_event = target[1]
                    for actual_event in recent_events:
                        if self._are_events_equivalent(actual_event, target_event):
                            self.attribute_changes[0].remove(target)
                else:
                    shape = self.parts[0]
                    current_value = getattr(shape, target[0])
                    if target[1] == current_value:
                        self.attribute_changes[0].remove(target)
                        
                    else:
                        if target[0] == 'radius':
                            if current_value > target[1]:
                                shape.unsafe_set_radius(current_value - 1)
                            else:
                                shape.unsafe_set_radius(current_value + 1)
                        else:
                            if current_value > target[1]:
                                setattr(shape, target[0], current_value - 1)
                            else:
                                setattr(shape, target[0], current_value + 1)
                
                if not self.attribute_changes[0]:
                    self.attribute_changes = self.attribute_changes[1:]
                    break
    
    @staticmethod
    def _are_events_equivalent(actual_event:ActionEvent, target_event:ActionEvent):
        'Returns a boolean stating if the two events are equivalent or not'

        for attr in ['affected_attribute', 'attribute_outcome']:

            attr_1 = actual_event.__getattribute__(attr)
            attr_2 = target_event.__getattribute__(attr)

            if (attr_1 != attr_2):
                return False
        
        return True