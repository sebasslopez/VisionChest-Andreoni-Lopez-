from typing import TYPE_CHECKING
import pygame


if TYPE_CHECKING:
    import VisionChest as vision
    import gui.screen.screen as screen

class menuScreen(screen.Screen):
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
        if(key == pygame.K_ESCAPE and self.last_screen != None):vision.setScreen(self.last_screen)
        elif(key == pygame.K_LEFT):vision.setScreen(screen.Screen(self.width, self.height, self))
        super().handleKeyPress(self,key)