import ctypes
import pygame.font
import pymunk

from pymunk_cd import utilities

from .primitives import Primitives 

from .action_event import ActionEvent
from .CompoundEntity import CompoundEntity
from .definitions.primitives import dictionary as prim_dictionary
from .definitions.verbs import dictionary as verb_dictionary

import typing

class CDManager:
    'Tracks all CompoundEntity instances, acts when a CD event is detected'
    def __init__(self, screen:pygame.surface.Surface, space:pymunk.Space):
        self.screen = screen
        self.space = space

        self.objects = [] 
        self.distance_matrices = []
        return

    def get_entity_index(self, entity:CompoundEntity):
        return self.objects.index(entity)

    def tick(self):
        #create distance matrix
        distance_matrix = utilities.square_matrix(len(self.objects))

        for i in range(len(self.objects)):
            obj = self.objects[i]
            obj_cog = obj.get_centre_of_gravity()

            for j in range(len(self.objects)):
                if i == j or distance_matrix[i][j]:
                    continue
                other_obj_cog = self.objects[j].get_centre_of_gravity()
                distance = (other_obj_cog - obj_cog).get_length()
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance


        self.distance_matrices.append(distance_matrix)

        # objects to do regular tasks, and return any events
        for obj in self.objects:
            obj_cog = obj.get_centre_of_gravity()

            events = obj.tick(self)
            if events:
                for event in events:
                    
                    output_nl = False
                    if output_nl == True:
                        candidate_verbs = self.detect_scenarios(event)
                        
                        if len(candidate_verbs):
                            print(stringify_entity(event.subject)
                                + ' ' 
                                + candidate_verbs[0].sense_id 
                                + 's '
                                + stringify_entity(event.event_object)
                                )
                        else:
                            utilities.warn('No candiates verbs found for event!')
                    else:
                        primitive = self.find_primitive_for_action_event(event) 
                        print(stringify_entity(event.subject)
                                + ' <=> ' 
                                + primitive.name + ' ' 
                                + stringify_entity(event.event_object)
                                + '\n'
                                + '\t'+ event.affected_attribute.name                                 
                                + ((' -> ' + event.attribute_outcome.name) if event.attribute_outcome else '')
                                )

            if len(obj.parts) > 1:
                inclusion_radius = obj.get_inclusion_radius(obj_cog)
                pygame.draw.circle(self.screen,
                    (0,0,0),
                    utilities.to_pygame(obj_cog),
                    int(inclusion_radius),
                    1
                )
        
        
        return

    @staticmethod
    def find_primitive_for_action_event(event:ActionEvent):
        # Eliminate incompatible primitives
        eliminated_primitives = []
        selected_primitive = None
        for prim in Primitives:
            prim_def = prim_dictionary[prim]
            # for attr in ['affected_attribute', 'object_constraint', 'attribute_outcome']:
            
            attr_1 = event.affected_attribute
            attr_2 = prim_def.affected_attribute

            if attr_1 and attr_2 and (attr_1 != attr_2):
                eliminated_primitives.append(prim)
                continue
            
            outcome_1 = event.attribute_outcome
            outcome_2 = prim_def.attribute_outcome

            if outcome_1 and outcome_2 and (outcome_1 != outcome_2):
                eliminated_primitives.append(prim)
            else:
                assert selected_primitive == None, 'Shouldn\'t find multiple compatible primitives'
                selected_primitive = prim

            # TODO: implement object_constraint properly
        
        assert selected_primitive != None, 'Should find a compatible primitives'
        return selected_primitive

    @staticmethod
    def detect_scenarios(event:ActionEvent):
        '''Takes action events in and outputs candidate verbs to describe them'''
        
        selected_primitive = CDManager.find_primitive_for_action_event(event)            

        # Look up a verb to describe what's happened
        candidate_verbs = []
 
        # remaining_verbs = [verb_def for verb_def in verb_dictionary if verb_def.primitive not in eliminated_primitives]
        for verb_def in verb_dictionary.values():
            if (verb_def.primitive != selected_primitive):
                continue

            if (event.affected_attribute == verb_def.affected_attribute) and (event.attribute_outcome == verb_def.attribute_outcome):
                candidate_verbs.append(verb_def)

        
        return candidate_verbs


    def display_text(self, message):
        # display text for event
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Arial", 30)
        # apply it to text on a label
        label = myfont.render(message, 1, (0,0,0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (100, 100))


def stringify_entity(entity : typing.Union[CompoundEntity, pymunk.Shape]):
    if type(entity) == CompoundEntity:
        return entity.__str__()
    elif entity is None:
        return ''
    else:
        return type(entity).__name__