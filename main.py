import pygame
import random
from pygame.locals import *
pygame.init()

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
running = True
bg_offset = 0
MAX_BRICK_HIGHT = 300  #! random value
MIN_BRICK_HIGHT = 600  #! random value
DIRECTION_RIGHT = "right"
DIRECTION_LEFT = "left"
STEPS = 2
change_direction = DIRECTION_RIGHT
WALK_LIMIT_RIGHT = 1400
WALK_LIMIT_LEFT = 50
bg_move = "False"

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        pygame.sprite.Sprite.__init__(self)
        original_player = pygame.image.load('./player.png')                                                        #? load the image from the files 
        original_player_size = original_player.get_size()                                                         #? get the size of the original image
        player_image = pygame.transform.scale(original_player, (original_player_size[0]/8, original_player_size[1]/8))  #? resize the image because it was too big
        player_size = player_image.get_size()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.player_size = player_size
        self.rect.x = pos_x  
        self.rect.y = pos_y
        self.direction = direction
        self.move_x=0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def control(self, steps):
        self.move_x = steps
       
    def update(self):
        self.rect.x = self.rect.x + self.move_x

    def gravity(self):
        self.move_y += gravity #? how fast the pl"
        if(self.rect.y > WORLD_FLOOR and self.move_y >= 0):
            self.move_y = 0

#generate player
player = Player(initial_pos_x, initial_pos_y, DIRECTION_RIGHT)


class Brick(pygame.sprite.Sprite):
    def __init__(self, brick_pos_x, brick_pos_y):
        pygame.sprite.Sprite.__init__(self)
        original_brick = pygame.image.load('./brick.png')
        original_brick_size = original_brick.get_size()
        brick = pygame.transform.scale(original_brick, (original_brick_size[0]*4, original_brick_size[1]*4))
        brick_size = brick.get_size()
        self.image = brick
        self.rect = self.image.get_rect()
        self.brick_size = brick_size
        self.brick_pos_x = brick_pos_x
        self.brick_pos_y = brick_pos_y

#generate draw bricks on screen
brick_group = pygame.sprite.Group()
if('condition happens'): #! find a condition
    new_brick = Brick(random.randrange(EDGE_LEFT, EDGE_RIGHT) ,random.randrange(MAX_BRICK_HIGHT, MIN_BRICK_HIGHT))
    brick_group.add(new_brick)
brick_group.draw(screen)


while running:

    for event in pygame.event.get():
        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame .K_UP:
                change_to = UP

            if event.key == pygame.K_RIGHT:
                change_direction = DIRECTION_RIGHT
                player.control(STEPS)
                bg_move = "Right"

            if event.key == pygame.K_LEFT:
                change_direction = DIRECTION_LEFT
                player.control(-STEPS)
                bg_move = "Left"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.control(0)
                bg_move = "False"

            if event.key == pygame.K_LEFT:
                player.control(0)
                bg_move = "False"

        #close the game
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    

    if((player.rect.x > WALK_LIMIT_RIGHT) and (bg_move == "Right")): 
        bg_offset -= 1.5
        player.control(0)

    if(player.rect.x < WALK_LIMIT_LEFT and (bg_move == "Left")):
        bg_offset += 1.5
        player.control(0)

    screen.blit(bg_img, (bg_offset, 0))
    screen.blit(bg_img, (EDGE_RIGHT + bg_offset, 0))
    screen.blit(bg_img, (-EDGE_RIGHT + bg_offset, 0))

    if (bg_offset <= -EDGE_RIGHT):
        screen.blit(bg_img, (EDGE_RIGHT + bg_offset, 0))
        bg_offset = 0
    if (bg_offset >= EDGE_RIGHT):
        screen.blit(bg_img, (-EDGE_RIGHT + bg_offset, 0))
        bg_offset = 0

    if(player.direction != change_direction):
        player.direction = change_direction
        player.flip()
    
    player.update()

    screen.blit(player.image, (player.rect.x, player.rect.y))

    pygame.display.update()
    

pygame.quit()