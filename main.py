import time
import pygame
import sys
from pygame.locals import *
from player import Player
from enemy import Enemy

#Initialize Pygame
pygame.init()

#Set up the window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("DoubleEdge Sword")

#Make the player and enemy
player = Player("player.png", 100, 100, 100, 100)
enemy = Enemy("enemy.png", 100, 100, 100, 100)

#Start the game loop
while True:
    #Make the background black
    screen.fill((0, 0, 0))
    #Add the player and enemy onto the screen
    player.draw(screen)
    enemy.draw(screen)

    #Check for events to see if the player wants to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    #Check for key presses to move the player
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.x -= 8
    if keys[K_RIGHT]:
        player.x += 8

    #Add cooldown to jump
    current_time = time.time()
    #Check for key presses to make the player jump
    if not player.is_jump and keys[K_UP] and (current_time - player.last_time) > 1:
       player.is_jump = True
       player.last_time = current_time
    #Logic to change how the player jumps
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

    #Make the enemy move towards the player
    enemy.moveTowardPlayer(enemy.x, player.x)
    #Control frame rate
    pygame.time.delay(5)
    #Update the display
    pygame.display.update()