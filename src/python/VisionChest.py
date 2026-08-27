import pygame
from gui.screen.screen import Screen
from gui.screen.boardScreen import boardScreen

class VisionChest:
    
    instance: "VisionChest | None" = None
    def __init__(self):
        VisionChest.instance = self
        self.screenSize = (800,600)
        pygame.init()
        self.screenwindow :pygame.Surface | None = pygame.display.set_mode(self.screenSize, pygame.RESIZABLE)
        self.clock:pygame.time.Clock | None = pygame.time.Clock()
        self.screen = boardScreen(self.screenSize)
        pygame.display.set_caption("VisionChest")
        self.running = True
        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                update:bool = False
                if (event.type == pygame.QUIT): 
                    self.running = False
                if(event.type == pygame.WINDOWRESIZED):
                    size = pygame.display.get_window_size()
                    self.width = size[0]
                    self.heigh = size[1]
                    update = True
                if(self.screen != None): 
                    self.screen.handle_event(event)
                    if update and self.screenwindow != None:
                        self.screen.update(self.screenwindow,self.screenSize)
            if(self.screenwindow != None and self.screen != None): 
                self.screen.display(self.screenwindow)
            pygame.display.flip()
            if(self.clock != None): self.clock.tick(60)
        pygame.quit()

    def setScreen(self,new_screen: Screen | None):
        self.screen = new_screen

    def getScreen(self) -> Screen | None:
        return self.screen

    @staticmethod
    def getInstance() -> "VisionChest":
        if(VisionChest.instance == None):
            return VisionChest()
        return VisionChest.instance
        

if __name__ == "__main__":
    VisionChest()
