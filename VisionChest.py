import pygame
import gui.screen.screen as SCREEN
class VisionChest:
    HEIGHT:int = 600
    WIDTH:int = 800
    window: pygame.Surface | None = None
    clock = None
    running = False
    screen: SCREEN.Screen | None = None
    instance = None
    def __init__(self):
        pygame.init()
        self.screenwindow = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.screen = SCREEN.Screen(self.WIDTH, self.HEIGHT, None)
        pygame.display.set_caption("VisionChest")
        self.running = True
        self.instance = self
        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): self.running = False
                if(self.screen != None): self.screen.handle_event(event)
            if(self.window != None): self.window.fill((0, 0, 255))
            pygame.display.flip()
            if(self.clock != None): self.clock.tick(60)
        pygame.quit()

    def setScreen(self,new_screen: SCREEN.Screen | None):
        self.screen = new_screen

    def getScreen(self) -> SCREEN.Screen | None:
        return self.screen

    @staticmethod
    def geInstance() -> "VisionChest":
        if(VisionChest.instance == None):
            return VisionChest()
        return VisionChest.instance


    @staticmethod
    def main():
        VisionChest()
    