import pygame
from ...chess import Board as boar
from .screen import Screen

Board: boar.Board = boar.Board()
    
class boardScreen(Screen):
    def __init__(self, size:tuple[int,int]):
        super().__init__(size, None)

    def handle_event(self, event: pygame.event.Event):
        pass

    def display(self, window: pygame.Surface):
        window.fill((0, 255, 255),(0,0,15,15))
        pass

    def update(self, window: pygame.Surface,size:tuple[int,int]):
        super().clear(window)
        self.display(window)
        pygame.display.flip()

    def handleKeyPress(self,key: int):
        super().handleKeyPress(key)