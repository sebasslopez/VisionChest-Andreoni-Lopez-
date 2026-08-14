import pygame
import gui.screen.screen as SCREEN

HEIGHT = 600
WIDTH = 800
window: pygame.Surface | None = None
clock = None
running = False
screen: SCREEN.Screen | None = None

    
def __init__():
    global window, clock, running, screen
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    screen = SCREEN.Screen(WIDTH, HEIGHT, None)
    pygame.display.set_caption("VisionChest")
    running = True

def main():
    global window, clock, running, screen
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): running = False
            if(screen != None): screen.handle_event(event)
        if(window != None): window.fill((0, 0, 255))
        pygame.display.flip()
        if(clock != None): clock.tick(60)
    pygame.quit()

@staticmethod
def setScreen(new_screen: SCREEN.Screen | None):
    global screen
    screen = new_screen

__init__()
main()