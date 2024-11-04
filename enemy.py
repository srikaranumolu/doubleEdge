import pygame

class Enemy:
    def __init__(self, image, x, y, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.is_jumping = False
        self.speed = 4
        self.health = 100


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def moveTowardPlayer(self,xen,xpy,speed):
        if (xen> xpy):
            self.x -= speed

        if (xen < xpy):
            self.x += speed

    def backOnScreen(self,screen,x):
        if(x < 0):
            self.x = screen.get_width()
        elif(x > screen.get_width()):
            self.x = 0



