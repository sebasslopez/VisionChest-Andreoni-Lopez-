from __future__ import annotations
import pygame

class Screen():
    def __init__(self, size:tuple[int,int], last_screen: Screen | None = None):
        self.screenSize = (size[0],size[1])
        self.last_screen = last_screen
        import VisionChest as VisionChest
        self.vision = VisionChest.VisionChest.getInstance()

    def handle_event(self, event: pygame.event.Event):
        if(event.type == pygame.KEYDOWN): self.handleKeyPress(event.key)
        elif(event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]): self.handleMouseClick(event.pos)
        pass

    def display(self, window: pygame.Surface):
        window.fill((0, 0, 255))
        pass

    def update(self, window: pygame.Surface,size:tuple[int,int]):
        self.clear(window)
        self.display(window)
        self.width = size[0]
        self.height = size[1]
        pygame.display.flip()

    def clear(self, window: pygame.Surface):
        window.fill((0,0,0))

    def handleKeyPress(self,key: int):
        if(key == pygame.K_ESCAPE and self.last_screen != None):self.vision.stop()
        elif(key == pygame.K_RIGHT):
            from gui.screen.menuScreen import menuScreen
            self.vision.setScreen(menuScreen(self.screenSize))
        pass

    def handleMouseClick(self,rect:tuple[int,int]):
        pass