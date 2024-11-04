import time
import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("DoubleEdge Sword")

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

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

x = 200
y = 200

player = Player("player.png", x, y, 100, 100)

while True:
    screen.fill((0, 0, 0))
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.x -= 5
    if keys[K_RIGHT]:
        player.x += 5
    current_time = time.time()
    if not player.is_jump and keys[K_UP] and (current_time - player.last_time) > 1:
            player.is_jump = True
            player.last_time = current_time
    if player.is_jump:
        F = (1/2) * player.mass * (player.velocity_y ** 2)
        player.y-=F
        player.velocity_y-=0.5
        if player.velocity_y < 0:
            player.mass = -1
        if player.velocity_y == -7:
            player.is_jump = False
            player.velocity_y = 6
            player.mass = 1
            player.y = player.og

    pygame.time.delay(10)
        # Draw the player
    pygame.display.update() # Update the display