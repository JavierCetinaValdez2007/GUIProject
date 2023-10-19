import pygame 

class Car(pygame.sprite.Sprite):
    def __init__(self, STARTX, STARTY, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.width = 30
        self.height = 20
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
    def update(self, keys):
        up = keys[pygame.K_w] 
        down = keys[pygame.K_s]
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]

        move = pygame.math.Vector2(right - left, down - up)

        if move.length_squared() > 0:
            move.scale_to_length(self.speed)
            self.pos += move
            self.rect.topleft = round(self.pos.x), round(self.pos.y)
            

        if self.rect.left < 0:
            self.rect.left = 5
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH-5
        if self.rect.top <= 0:
            self.rect.top = 5
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT-5