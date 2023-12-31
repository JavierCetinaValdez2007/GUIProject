import pygame
from Player import Player
from Car import Car
from random import randrange
def main():
   
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    x = randrange(5,6)
    y = randrange(3,4)
    z = randrange(1,2)

    beginning = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
    car1 = Car(beginning,SCREEN_HEIGHT/x,SCREEN_WIDTH,SCREEN_HEIGHT)
    car2 = Car(beginning,SCREEN_HEIGHT/y,SCREEN_WIDTH,SCREEN_HEIGHT)
    car3 = Car(beginning,SCREEN_HEIGHT/z,SCREEN_WIDTH,SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    car1.end = (SCREEN_WIDTH)
    car2.end = (SCREEN_WIDTH)
    car3.end = (SCREEN_WIDTH)
    clock = pygame.time.Clock()
    running = True

    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    allSprites.add(car1)
    allSprites.add(car2)
    allSprites.add(car3)

    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        pressedKeys = pygame.key.get_pressed()
        player.update(pressedKeys)
        screen.fill((255,255,255))
        allSprites.draw(screen)
        pygame.display.flip()

        if(pygame.sprite.collide_rect(player,car1)) or (pygame.sprite.collide_rect(player,car2)) or (pygame.sprite.collide_rect(player,car3)):
            running = False
        clock.tick(30)
        #for i in range(clock.tick):
            

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
