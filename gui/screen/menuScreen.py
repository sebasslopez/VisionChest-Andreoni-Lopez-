import pygame
from gui.screen.Screen import Screen


class menuScreen(Screen):
    def __init__(self, width: int, height: int):
        super().__init__(width, height, None)
        

    def handle_event(self, event: pygame.event.Event):
        pass

    def display(self, window: pygame.Surface):
        window.fill((0, 255, 255))
        pass

    def update(self, window: pygame.Surface):
        self.display(window)
        pygame.display.flip()

    def handleKeyPress(self,key: int):
        if(key == pygame.K_ESCAPE and self.vision.getScreen != None): self.vision.setScreen(menuScreen(self.width,self.height))
        elif(key == pygame.K_LEFT and self.vision.getScreen != None): self.vision.setScreen(Screen(self.width, self.height, self))
        super().handleKeyPress(key)