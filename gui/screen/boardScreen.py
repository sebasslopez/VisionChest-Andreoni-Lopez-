from typing import TYPE_CHECKING
import pygame

Board: 

if TYPE_CHECKING:
    import VisionChest as vision
    import gui.screen.screen as screen

class boardScreen(screen.Screen):
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
        super().handleKeyPress(self,key)