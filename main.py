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

# game speed
fps = pygame.time.Clock()
player_speed = 200

# background image	
bg_img = pygame.image.load('./bg.jpeg')
bg_img = pygame.transform.scale(bg_img,(EDGE_RIGHT,EDGE_BOTTOM))


# This is a list of 'sprites.' Each block in the program is added to this list.
block_list = pygame.sprite.Group()

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()  #? All blocks and the player block as well.


# initial_pos
initial_pos_x = 50  
initial_pos_y = 660   


# initial settings
GRAVITY = 0.25
WORLD_FLOOR = 660 
running = True
bg_offset = 0
DIRECTION_RIGHT = "right"
DIRECTION_LEFT = "left"
STEPS = 2
change_direction = DIRECTION_RIGHT
WALK_LIMIT_RIGHT = 1400
WALK_LIMIT_LEFT = 50
bg_move = False
INITIAL_JUMP_SPEED = -12
TOP_PLATFORM_HEIGHT = 250
BOTTOM_PLATFORM_HEIGHT = 550
PLATFORM_SPACE = 70
BLOCK = "block"
SHORT_PLATFROM = "short_platform"
LONG_PLATFORM = "long_platform"


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        pygame.sprite.Sprite.__init__(self)
        original_player = pygame.image.load('./player.png')                                                        
        original_player_size = original_player.get_size()                                                        
        player_image = pygame.transform.scale(original_player, (original_player_size[0]/10, original_player_size[1]/10))  
        player_size = player_image.get_size()

        self.image = player_image
        self.rect = self.image.get_rect()
        self.player_size = player_size
        self.rect.x = pos_x  
        self.rect.y = pos_y
        self.direction = direction
        self.move_x = 0
        self.move_y = 0
        self.is_jumping = False 
        self.is_falling = False
        self.to_jump = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def control(self, steps):
        self.move_x = steps

    def jump(self):
        if(self.is_jumping):
            if(self.is_falling == False and self.move_y == 0):
                self.move_y = INITIAL_JUMP_SPEED
            elif((self.move_y + GRAVITY) >= 0):
                self.move_y += GRAVITY
                self.is_falling = True
                self.is_jumping = False
            elif(self.is_falling == False and self.move_y != 0):
                self.move_y += GRAVITY

        if(self.is_falling):
            if(self.rect.y + (self.move_y + GRAVITY) > WORLD_FLOOR):
                self.move_y = 0
                self.rect.y = WORLD_FLOOR
                self.is_falling = False
            else:
                self.move_y += GRAVITY
      
    def update(self):
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y

#generate player
player = Player(initial_pos_x, initial_pos_y, DIRECTION_RIGHT)
all_sprites_list.add(player)



class Block(pygame.sprite.Sprite):
    def __init__(self, block_pos_x, block_pos_y):
        pygame.sprite.Sprite.__init__(self)
        original_block = pygame.image.load('./block.png')
        original_block_size = original_block.get_size()
        block = pygame.transform.scale(original_block, (original_block_size[0]*4, original_block_size[1]*4))
        block_size = block.get_size()

        self.image = block
        self.rect = self.image.get_rect()
        self.block_size = block_size
        self.rect.x = block_pos_x
        self.rect.y = block_pos_y

 
class Short_platform(pygame.sprite.Sprite):
    def __init__(self, short_platform_pos_x, short_platform_pos_y):
        pygame.sprite.Sprite.__init__(self)
        original_short_platform = pygame.image.load('./short_platform.png')
        original_short_platform_size = original_short_platform.get_size()
        short_platform = pygame.transform.scale(original_short_platform, (original_short_platform_size[0]*4, original_short_platform_size[1]*4))
        short_platform_size = short_platform.get_size()

        self.image = short_platform
        self.rect = self.image.get_rect()
        # self.size
        self.short_platform_size = short_platform_size
        self.rect.x = short_platform_pos_x
        self.rect.y = short_platform_pos_y

    def update(self):
        self.rect.x -= 2
        if(self.rect.right < EDGE_LEFT):
            self.kill()




class Long_platform(pygame.sprite.Sprite):
    def __init__(self, long_platform_pos_x, long_platform_pos_y):
        pygame.sprite.Sprite.__init__(self)
        original_long_platform = pygame.image.load('./long_platform.png')
        original_long_platform_size = original_long_platform.get_size()
        long_platform = pygame.transform.scale(original_long_platform, (original_long_platform_size[0]*4, original_long_platform_size[1]*4))
        long_platform_size = long_platform.get_size()

        self.image = long_platform
        self.rect = self.image.get_rect()
        # self.size
        self.long_platform_size = long_platform_size
        self.rect.x = long_platform_pos_x
        self.rect.y = long_platform_pos_y

# print(EDGE_RIGHT//5)
# l = random.choice(('test1', 'test2', 'test3'))
# short_platform = Short_platform(300, 300)
# print(short_platform.rect.right - short_platform.rect.left)

for segment in range(5):
        short_platform = Short_platform(random.randrange(EDGE_RIGHT + EDGE_RIGHT//5*segment + 10, EDGE_RIGHT + EDGE_RIGHT // 5 * (segment + 1) - 10), TOP_PLATFORM_HEIGHT)
        block_list.add(short_platform)

# last_sprite = block_list.sprites()[-1]
# print(last_sprite.rect.right)

while running:
    for event in pygame.event.get():
        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame .K_UP:
                player.is_jumping = True

            if event.key == pygame.K_RIGHT:
                change_direction = DIRECTION_RIGHT
                player.control(STEPS)
                bg_move = DIRECTION_RIGHT

            if event.key == pygame.K_LEFT:
                change_direction = DIRECTION_LEFT
                player.control(-STEPS)
                bg_move = DIRECTION_LEFT

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.control(0)
                bg_move = False

            if event.key == pygame.K_LEFT:
                player.control(0)
                bg_move = False

        #close the game
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if(player.rect.x < WALK_LIMIT_LEFT and (bg_move == DIRECTION_LEFT)):
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

    
    last_sprite = block_list.sprites()[-1]
    if(last_sprite.rect.right < 1400):

        for segment in range(5):
            short_platform = Short_platform(random.randrange(EDGE_RIGHT + EDGE_RIGHT//5*segment + 10, EDGE_RIGHT + EDGE_RIGHT // 5 * (segment + 1) - 10), TOP_PLATFORM_HEIGHT)
            block_list.add(short_platform)


    if((player.rect.x > WALK_LIMIT_RIGHT) and (bg_move == DIRECTION_RIGHT)): 
            bg_offset -= 1.5
            player.control(0)
            for block in block_list:
                block.update()

    print("bg offest: " + str(bg_offset))  
    for block in block_list:
        print("block " + str(last_sprite.rect.x))

    player.jump()
    player.update()

    all_sprites_list.draw(screen)
    block_list.draw(screen)
    
    pygame.display.update()
    fps.tick(player_speed)
    

pygame.quit()