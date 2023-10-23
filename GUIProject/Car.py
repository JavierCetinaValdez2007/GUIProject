import pygame 
from random import randrange
class Car(pygame.sprite.Sprite):
    def __init__(self, STARTX, STARTY, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.t = 0
        self.width = 30
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.end = (SCREEN_WIDTH)
        self.speed = 1
        #color
        self.image.fill((0,0,0))

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        startY = STARTY
        startX = STARTX

        self.pos = pygame.math.Vector2(startX,startY)
        self.center_pos = pygame.math.Vector2(
            startX + (self.width/2),
            startY + (self.height/2)
        )
        self.rect = self.image.get_rect(
            center = (startX/2,startY/2)
        )
        if self.pos.x < SCREEN_WIDTH:
            self.pos.x += 40
        