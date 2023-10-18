import pygame
from Player import Player
def main():
    allSprites = pygame.sprite.Group()    
    allSprites.add(Player)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255,255,255))
        allSprites.draw(screen)
        pygame.display.flip()
    
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
