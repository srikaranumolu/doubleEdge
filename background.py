import pygame
import math

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

# Define player variables
player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 70)
player_speed = 5
player_start_x = player_pos.x  # Initial player position

# Game loop
run = True
while run:
    clock.tick(FPS)

    # Update player position based on key presses
    keys = pygame.key.get_pressed()
    previous_x = player.x  # Store the player's previous x position

    # Update scroll based on player position change
    dx = player.x - previous_x  # Difference in player position
    scroll -= dx  # Adjust scroll based on this difference

    # Ensure infinite scrolling effect
    scroll = scroll % bg_width

    # Draw scrolling background
    for i in range(-1, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # Draw player (for simplicity, a rectangle representing the player)
    pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH / 2, player.y, 50, 50))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
