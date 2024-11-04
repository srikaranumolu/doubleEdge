import time
import pygame
import sys
import math
from pygame.locals import *
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

# Set up the window with a larger size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DoubleEdge Sword")

# Load and scale background image to fill the screen
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_width = bg.get_width()
bg_height = bg.get_height()

# Make background variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
width = 300
height = 300
# Make the player and enemy
player = Player("player.png", 164, 558, width, height)
enemy = Enemy("enemy.png", 0, 558, 250, 250)

# Variable to control jump height
jump_height = 8

def draw_health_bar(screen, x, y, health, max_health):
    bar_width = 200
    bar_height = 20
    fill = (health / max_health) * bar_width
    outline_rect = pygame.Rect(x, y, bar_width, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(screen, (255, 0, 0), fill_rect)
    pygame.draw.rect(screen, (0, 0, 0), outline_rect, 2)

# Start the game loop
while True:
    # Control frame rate
    pygame.time.delay(5)
    # Make the background black
    screen.fill((0, 0, 0))
    # Draw scrolling background
    for i in range(-1, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # Add the player and enemy onto the screen
    player.draw(screen)
    enemy.draw(screen)

    # Draw the health bar
    draw_health_bar(screen,  20, 830, player.health, 90)

    # Check for events to see if the player wants to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Check for key presses to move the player
    keys = pygame.key.get_pressed()
    previous_x = player.x  # Store the player's previous x position
    if keys[K_LEFT]:
        player.x -= 5
    if keys[K_RIGHT]:
        player.x += 5

    # Update scroll based on player position change
    dx = player.x - previous_x  # Difference in player position
    scroll -= dx  # Adjust scroll based on this difference

    # Add cooldown to jump
    current_time = time.time()
    # Check for key presses to make the player jump
    if not player.is_jump and keys[K_UP] and (current_time - player.last_time) > 1:
       player.is_jump = True
       player.last_time = current_time
       player.velocity_y = jump_height  # Set initial jump velocity to jump_height

    # Logic to change how the player jumps
    if player.is_jump:
        F = (1/2) * player.mass * (player.velocity_y ** 2)
        player.y -= F
        player.velocity_y -= 0.3  # Decrease the rate of change for smoother animation
        if player.velocity_y < 0:
            player.mass = -1
        if player.velocity_y <= -jump_height:  # Use jump_height variable
            player.is_jump = False
            player.velocity_y = jump_height  # Reset to jump_height
            player.mass = 1
            player.y = player.og  # Reset to original ground level

    # Ensure the player stays on the ground
    if player.y > player.og:
        player.y = player.og
        player.is_jump = False
        player.velocity_y = jump_height  # Reset to jump_height
        player.mass = 1

    # Make the enemy move towards the player
    enemy.moveTowardPlayer(enemy.x, player.x)

    if (abs(player.x - enemy.x) < 14):
        if (abs(player.y - enemy.y) < 14):
            player.health -= 10
            if (enemy.x == 0):
                player.x = SCREEN_WIDTH
            elif(enemy.x == SCREEN_WIDTH):
                player.x = 0
            else:
                player.x = 0

    enemy.backOnScreen(screen, enemy.x)
    if (player.health < 0):
        quit()

    # Update the display
    pygame.display.update()