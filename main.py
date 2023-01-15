import pygame
from pygame.locals import *
pygame.init()



# display resolution
edge_left = 0
edge_right = 1600
edge_top = 0
edge_bottom = 900
screen = pygame.display.set_mode((edge_right, edge_bottom))


# backround image	
bg_img = pygame.image.load('C:\School\Meditatii\Info')
bg_img = pygame.transform.scale(bg_img,(edge_right,edge_bottom))


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                running = False

    # refreshing the display
    pygame.display.update()


pygame.quit()