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
            self.x -= 3
        if (xen < xpy):
            self.x += 3

    def collision(self, player):
        if (self.x < player.x + player.image.get_width() and
            self.x + self.image.get_width() > player.x and
            self.y < player.y + player.image.get_height() and
            self.y + self.image.get_height() > player.y):
            return True


