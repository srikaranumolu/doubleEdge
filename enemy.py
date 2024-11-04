import pygame

class Enemy:
    def __init__(self, image, x, y, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.is_jumping = False


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def moveTowardPlayer(self,xen,xpy):
        if (xen> xpy):
            self.x -= 25
        if (xen < xpy):
            self.x += 25

