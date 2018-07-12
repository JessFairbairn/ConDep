import pygame.font

class CDManager:
    def __init__(self, screen):
        self.objects = []
        self.screen = screen
        return


    def tick(self):
        for obj in self.objects:
            events = obj.tick()
            if events:
                # display text for event
                # pick a font you have and set its size
                myfont = pygame.font.SysFont("Arial", 30)
                # apply it to text on a label
                label = myfont.render(events[0].type.name + " event!", 1, (0,0,0))
                # put the label object on the screen at point x=100, y=100
                self.screen.blit(label, (100, 100))

        return