import pygame
import math
from player import Player
from enemy import Enemy
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load image
bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()
bg_height = bg.get_height()

# Define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


# Game loop
run = True
while run:
    clock.tick(FPS)

    # Update player position based on key presses
    keys = pygame.key.get_pressed()
    previous_x = Player.x  # Store the player's previous x position

    # Update scroll based on player position change
    dx = Player.x - previous_x  # Difference in player position
    scroll -= dx  # Adjust scroll based on this difference

    # Ensure infinite scrolling effect
    scroll = scroll % bg_width

    # Draw scrolling background
    for i in range(-1, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # Draw player (for simplicity, a rectangle representing the player)
    pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH / 2, Player.y, 50, 50))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
