from __future__ import annotations
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import VisionChest as vision
    import gui.screen.menuScreen as menuScreen

class Screen():
    def __init__(self, width:int, height:int, last_screen: Screen | None = None):
        self.width = width
        self.height = height
        self.last_screen = last_screen

    def handle_event(self, event: pygame.event.Event):
        if(event.type == pygame.KEYDOWN): self.handleKeyPress(event.key)
        pass

    def display(self, window: pygame.Surface):
        window.fill((0, 0, 255))
        pass

    def update(self, window: pygame.Surface):
        self.display(window)
        pygame.display.flip()

    def handleKeyPress(self,key: int):
        if(key == pygame.K_ESCAPE and self.last_screen != None):vision.setScreen(self.last_screen)
        elif(key == pygame.K_RIGHT):vision.setScreen(menuScreen.menuScreen(self.width, self.height))
        pass