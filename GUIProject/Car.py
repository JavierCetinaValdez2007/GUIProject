import pygame 

class Car(pygame.sprite.Sprite):
    def __init__(self, STARTX, STARTY, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.width = 10
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.end = (SCREEN_WIDTH)
        self.speed = 10
        #color
        self.image.fill((0,0,0))

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT


        startX = STARTX
        startY = STARTY

        self.rect = self.image.get_rect(
            center = (startX, startY)
        )

        self.pos = pygame.math.Vector2(startX,startY)
        self.center_pos = pygame.math.Vector2(
            startX + (self.width),
            startY + (self.height/2)
        )
        if(self.end):
            startX += self.speed
