import pygame
from pygame.locals import *
pygame.init()


# display resolution
edge_left = 0
edge_right = 1600
edge_top = 0
edge_bottom = 900
screen = pygame.display.set_mode((edge_right, edge_bottom))

#game name
pygame.display.set_caption('Mega Giani Cousins')


# backround image	
bg_img = pygame.image.load('./bg.jpeg')
bg_img = pygame.transform.scale(bg_img,(edge_right,edge_bottom))
i = 0

# Giani
big_giani = pygame.image.load('./giani.png')                                           #? load the image from the files 
big_giani_size = big_giani.get_size()                                                  #? get the size of the original image
giani = pygame.transform.scale(big_giani, (big_giani_size[0]/8, big_giani_size[1]/8))  #? resize the image because it was too big
pos_x = 50
pos_y = 630

#gamplay
gravity = 1
move_right = False
move_left = False

runing = True
while runing:

    #move right
    if move_right:
        i -= 1
    screen.blit(bg_img, (i,0))
    screen.blit(bg_img, (edge_right + i, 0))
    if (i == -edge_right):
        screen.blit(bg_img, (edge_right + i, 0))
        i = 0

    #!move left
    if move_left:
        i += 1
    screen.blit(bg_img, (i,0))
    screen.blit(bg_img, (edge_right + i, 0))
    if (i == edge_left):
        screen.blit(bg_img, (0, 0))
        i = 0
    

    #show Giani on screen
    screen.blit(giani, (pos_x, pos_y))

    for event in pygame.event.get():

        #movement
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                change_to = "up"

            if event.key == pygame.K_RIGHT:
                move_right = True

            if event.key == pygame.K_LEFT:
                move_left = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                move_right = False

            if event.key == pygame.K_LEFT:
                move_left = False
        

        #close the game
        if event.type == QUIT:
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runing = False

    pygame.display.update()

pygame.quit()