import pygame
import sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (0, 0)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Character Example")

class Player:
    def __init__(self, image, x, y, width, height):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

player = Player("player.png", 100, 100, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((0, 0, 0))  # Clear the screen with black color
    player.draw(screen)     # Draw the player
    pygame.display.update() # Update the display