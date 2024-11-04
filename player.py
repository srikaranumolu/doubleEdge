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
        self.hit_count = 0  # Track the number of hits

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def kill(self, x, y, screen, enemy):
        radius = 140
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius, 10)
        distance = math.sqrt((x - enemy.x) ** 2 + (y - enemy.y) ** 2)
        if distance < radius:
            self.hit_count += 1
            if self.hit_count >= 3:
                self.BroadCastKill = True
                return True  # Indicate that the enemy is killed
        return False  # Indicate that the enemy is not killed