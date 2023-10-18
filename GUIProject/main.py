import pygame
running = True
pygame.init()
screen = pygame.display.set_mode((1000, 600))

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    screen.flip.display()
    

pygame.quit()