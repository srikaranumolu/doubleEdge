import pygame

class Player:
    def __init__(self, image, x, y, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.og = y
        self.velocity_y = 6
        self.is_jump = False
        self.mass = 1
        self.last_time = 0
        self.health = 100
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def kill(self,x,y,screen):
        pygame.draw.circle(screen, (255,0,0), (x,y), 100,10)
        pygame.time.delay(2000)