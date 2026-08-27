import pygame
from gui.screen.Screen import Screen
from gui.screen.BoardScreen import boardScreen
class VisionChest:
    
    instance: "VisionChest | None" = None
    def __init__(self):
        VisionChest.instance = self
        self.HEIGHT:int = 600
        self.WIDTH:int = 800
        pygame.init()
        self.screenwindow = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.screen = boardScreen(self.WIDTH, self.HEIGHT)
        pygame.display.set_caption("VisionChest")
        self.running = True
        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): 
                    self.running = False
                if(self.screen != None): 
                    self.screen.handle_event(event)
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


    @staticmethod
    def main():
        VisionChest()

if __name__ == "__main__":
    VisionChest.main()
