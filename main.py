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
screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("DoubleEdge Sword")

# Load and scale background image to fill the screen
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg, (1500, 900))
bg_width = bg.get_width()
bg_height = bg.get_height()

# Make background variables
scroll = 0
tiles = math.ceil(1500 / bg_width) + 1
width = 300
height = 300
# Make the player and enemy
player = Player("player.png", 164, 558, width, height)
enemy = Enemy("enemy.png", SCREEN_WIDTH, 558, 250, 250)

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
    if(player.BroadCastKill == False):
        enemy.draw(screen)

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
        player.x -= 7

    if keys[K_RIGHT]:
        player.x += 7

    # Update scroll based on player position change
    dx = player.x - previous_x  # Difference in player position
    scroll -= dx  # Adjust scroll based on this difference

    # Add cooldown to jump
    current_time = time.time()
    # Check for key presses to make the player jump
    if not player.is_jump and keys[K_UP] and (current_time - player.last_time) > 1:
       player.is_jump = True
       player.last_time = current_time
    # Logic to change how the player jumps
    if player.is_jump:
        F = (1/2) * player.mass * (player.velocity_y ** 2)
        player.y -= F
        player.velocity_y -= 0.5
        if player.velocity_y < 0:
            player.mass = -1
        if player.velocity_y == -7:
            player.is_jump = False
            player.velocity_y = 6
            player.mass = 1
            player.y = player.og

    # Make the enemy move towards the player
    enemy.moveTowardPlayer(enemy.x, player.x)

    if (abs(player.x - enemy.x) < 20):
        if (abs(player.y - enemy.y) < 20):
            player.health -= 10
            if (enemy.x < 200):
                player.x = SCREEN_WIDTH
            elif(enemy.x-200 > SCREEN_WIDTH):
                player.x = 0
            else:
                player.x = 0
    enemy.backOnScreen(screen, enemy.x)
    if (player.health < 0):
        quit()

    # Update the display
    if keys[K_SPACE]:
        player.kill(player.x+150,player.y+120,screen,enemy.x,enemy.y)

    pygame.display.update()