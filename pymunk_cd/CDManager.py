import ctypes
import pygame.font
from .EventType import EventType 


class CDManager:
    def __init__(self, screen):
        self.objects = []
        self.screen = screen
        return


    def tick(self):
        for obj in self.objects:
            events = obj.tick()
            if events:
                for event in events:
                    obj_name = event.object.name or ''
                    print(event.type.name + ' from object ' + obj_name)

                    if event.type == EventType.MOVE:
                        if event.part == "radius" and event.direction == "decrease":
                            print("Collapse event in " + event.object.name)                

        return

    def display_text(self, message):
        # display text for event
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Arial", 30)
        # apply it to text on a label
        label = myfont.render(message, 1, (0,0,0))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (100, 100))