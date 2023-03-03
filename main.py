import pygame
import random
from pygame.locals import *
pygame.init()


# constante cu CAPS
RIGHT = "right"
LEFT = "left"
UP = "up"
STILL = "still"

# display resolution
EDGE_LEFT = 0
EDGE_RIGHT = 1600
EDGE_TOP = 0
EDGE_BOTTOM = 900
screen = pygame.display.set_mode((EDGE_RIGHT, EDGE_BOTTOM))

# game name
pygame.display.set_caption('Mega Giani Cousins')


# background image	
bg_img = pygame.image.load('./bg.jpeg')
bg_img = pygame.transform.scale(bg_img,(EDGE_RIGHT,EDGE_BOTTOM))


# initial_pos
initial_pos_x = 50  
initial_pos_y = 630   


# initial settings
gravity = 1  #! random value (for now)
WORLD_FLOOR = 640  #! random value
change_to = STILL 
runing = True
bg_offset = 0
MAX_BRICK_HIGHT = 300  #! random value
MIN_BRICK_HIGHT = 600  #! random value

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        original_player = pygame.image.load('./player.png')                                                        #? load the image from the files 
        original_player_size = original_player.get_size()                                                         #? get the size of the original image
        player = pygame.transform.scale(original_player, (original_player_size[0]/8, original_player_size[1]/8))  #? resize the image because it was too big
        player_size = player.get_size()                                                             
        self.image_player = player
        self.player_size = player_size
        self.rect_x = pos_x  
        self.rect_y = pos_y

    def flip(self):
        self.flipped_image_player = pygame.transform.flip(self.image_player, True, False)

    def gravity(self):
        self.move_y += gravity #? how fast the player falls

        if(self.rect_y > WORLD_FLOOR and self.move_y >= 0):
            self.move_y = 0

#generate player
playerFacingRight = Player(initial_pos_x, initial_pos_y)
player_group = pygame.sprite.Group()
player_group.add(playerFacingRight)



class Brick(pygame.sprite.Sprite):
    def __init__(self, brick_pos_x, brick_pos_y):
        original_brick = pygame.image.load('.brick.png')
        original_brick_size = original_brick.get_size()
        brick = pygame.transform.scale(original_brick, (original_brick_size[0]*4, original_brick_size[1]*4))
        brick_size = brick.get_size()
        self.image_brick = brick
        self.brick_size = brick_size
        self.brick_pos_x = brick_pos_x
        self.brick_pos_y = brick_pos_y

#generate draw bricks on screen
brick_group = pygame.sprite.Group()
if('condition happens'): #! find a condition
    new_brick = Brick(random.randrange(EDGE_LEFT, EDGE_RIGHT) ,random.randrange(MAX_BRICK_HIGHT, MIN_BRICK_HIGHT))
    brick_group.add(new_brick)
brick_group.draw(screen)


while runing:
    if change_to == RIGHT:
        bg_offset -= 1

    if change_to == LEFT:
         bg_offset += 1

    screen.blit(bg_img, (bg_offset, 0))
    screen.blit(bg_img, (EDGE_RIGHT + bg_offset, 0))
    screen.blit(bg_img, (-EDGE_RIGHT + bg_offset, 0))

    if (bg_offset <= -EDGE_RIGHT):
        screen.blit(bg_img, (EDGE_RIGHT + bg_offset, 0))
        bg_offset = 0
    if (bg_offset >= EDGE_RIGHT):
        screen.blit(bg_img, (-EDGE_RIGHT + bg_offset, 0))
        bg_offset = 0
    

    for event in pygame.event.get():
        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = UP

            if event.key == pygame.K_RIGHT:
                change_to = RIGHT

            if event.key == pygame.K_LEFT:
                change_to = LEFT

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                change_to = STILL

            if event.key == pygame.K_LEFT:
                change_to = STILL
        

        #close the game
        if event.type == QUIT:
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runing = False

    pygame.display.update()
    player_group.draw(screen)

pygame.quit()