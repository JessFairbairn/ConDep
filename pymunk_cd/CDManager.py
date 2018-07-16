import ctypes
import pygame.font
from .Utilities import *

from .EventType import EventType 


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

    def detect_scenarios(self, event):
        if event.event_type == EventType.MOVE:
            if event.object == "radius" and event.direction == "decrease":
                print("Collapse event in " + event.subject.name)


    def display_text(self, message):
        # display text for event
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Arial", 30)
        # apply it to text on a label
        label = myfont.render(message, 1, (0,0,0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (100, 100))