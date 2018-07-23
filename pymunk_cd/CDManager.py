import ctypes
import pygame.font
from .Utilities import *

from .EventType import EventType 

from .action_event import ActionEvent
from .parsing.primitives import dictionary as prim_dictionary

# from parsing.cd_definitions.CD


class CDManager:
    'Tracks all CompoundEntity instances, acts when a CD event is detected'
    def __init__(self, screen, space):
        self.objects = []
        self.screen = screen
        self.space = space
        return


    def tick(self):
        for obj in self.objects:
            obj_cog = obj.get_centre_of_gravity()
            inclusion_radius = obj.get_inclusion_radius(obj_cog)

            events = obj.tick()
            if events:
                for event in events:
                    print(event)

                    self.detect_scenarios(event)

            pygame.draw.circle(self.screen, 
                (0,0,0),
                to_pygame(obj_cog),
                int(inclusion_radius),
                1
            )
        return

    def detect_scenarios(self, event:ActionEvent):
        
        # Eliminate incompatible primitives
        eliminated_primitives = []
        for prim in EventType:
            prim_def = prim_dictionary[prim]
            # for attr in ['affected_attribute', 'object_constraint', 'attribute_change_polarity']:
                
            attr_1 = event.affected_attribute
            attr_2 = prim_def.affected_attribute

            if attr_1 and attr_2 and (attr_1 != attr_2):
                eliminated_primitives.append(prim)
        
        
            # TODO: handle attribute_change_polarity better as it's boolean
            # TODO: implement object_constraint properly
        return
        


    def display_text(self, message):
        # display text for event
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Arial", 30)
        # apply it to text on a label
        label = myfont.render(message, 1, (0,0,0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (100, 100))