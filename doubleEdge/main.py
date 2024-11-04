import pygame
pygame.init()
x = 400
y = 400
screen = pygame.display.set_mode((x, y))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()

