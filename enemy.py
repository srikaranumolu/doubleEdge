# import pygame module in this program
import pygame
from pygame import K_ESCAPE, KEYDOWN

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white, green,
# blue, black, red '
# colour respectively.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

# assigning values to X and Y variable
X = 0
Y = 0

# create the display surface object
# of specific dimension..e(X,Y).
display_surface = pygame.display.set_mode((X, Y),pygame.FULLSCREEN)

# set the pygame window name
pygame.display.set_caption('DoubleEdge Sword')

# completely fill the surface object
# with white colour
display_surface.fill(blue)
enemyImage = pygame.image.load(r"enemy.png").convert_alpha()
enemy = pygame.transform.scale(enemyImage, (100,100))

display_surface.blit(enemy, (0, 0))
# draw a polygon using draw.polygon()
# method of pygame.
# pygame.draw.polygon(surface, color, pointlist, thickness)
# thickness of line parameter is optional.

# infinite loop
while True:

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if (event.type == pygame.QUIT):
            pygame.quit()

        # quit the program.
            quit()
        elif(event.type == KEYDOWN):
            if (event.key == K_ESCAPE):

            # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

        # Draws the surface object to the screen.
        pygame.display.update();
        if()

