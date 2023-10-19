import pygame
from Player import Player
from Car import Car
import random
def main():
   
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    x = random.randint(1,12)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
    car = Car(SCREEN_WIDTH/30,SCREEN_HEIGHT/x,SCREEN_WIDTH,SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    end = (SCREEN_WIDTH)
    clock = pygame.time.Clock()
    running = True

    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    allSprites.add(car)
    

    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        pressedKeys = pygame.key.get_pressed()
        player.update(pressedKeys)
        screen.fill((255,255,255))
        allSprites.draw(screen)
        pygame.display.flip()
        if(pygame.sprite.collide_rect(player,car)):
            running = False
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
