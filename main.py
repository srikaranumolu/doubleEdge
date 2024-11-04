import time
import pygame
import sys
from pygame.locals import *
from player import Player
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("DoubleEdge Sword")

player = Player("player.png", 200, 200, 100, 100)
enemy = Enemy("enemy.png", 100, 100, 100, 100)

while True:
    screen.fill((0, 0, 0))
    player.draw(screen)
    enemy.draw(screen)

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

    enemy.moveTowardPlayer(enemy.x, player.x)
    pygame.time.delay(10)
    pygame.display.update()