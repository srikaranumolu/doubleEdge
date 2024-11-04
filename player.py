import pygame
import math
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
        self.BroadCastKill = False
        self.win = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def kill(self, x, y, screen, enx, eny, enh):
        radius = 140
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius, 10)
        distance = math.sqrt((x - enx) ** 2 + (y - eny) ** 2)
        if distance < radius:
            if enh <= 0:
                self.BroadCastKill = True
            enh -= 34
            self.health -= 1
