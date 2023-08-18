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


# sprite gorups
block_list = pygame.sprite.Group()
money_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


# initial_pos
initial_pos_x = 50  
initial_pos_y = 693   


# initial settings
GRAVITY = 0.20
WORLD_FLOOR = 693 
running = True
bg_offset = 0
DIRECTION_RIGHT = "right"
DIRECTION_LEFT = "left"
STEPS = 2
change_direction = DIRECTION_RIGHT
WALK_LIMIT_RIGHT = 1400
bg_move = False
INITIAL_JUMP_SPEED = -15
TOP_PLATFORM_HEIGHT = 250
BOTTOM_PLATFORM_HEIGHT = 600


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

class Money(pygame.sprite.Sprite):
    def __init__(self, money_pos_x, money_pos_y):
        pygame.sprite.Sprite.__init__(self)
        original_money = pygame.image.load('./money.png')
        original_money_size = original_money.get_size()
        money = pygame.transform.scale(original_money, (original_money_size[0]*2, original_money_size[1]*2))
        
        self.image = money
        self.rect = self.image.get_rect()
        self.rect.x = money_pos_x
        self.rect.y = money_pos_y

    def update(self):
        self.rect.x -= 2
        if(self.rect.right < EDGE_LEFT):
            self.kill()



for segment in range(4):
        short_platform = Short_platform(random.randrange(EDGE_RIGHT + EDGE_RIGHT / 4 * segment + 100, EDGE_RIGHT + EDGE_RIGHT / 4 * (segment + 1) - 100), random.randrange(TOP_PLATFORM_HEIGHT, BOTTOM_PLATFORM_HEIGHT))
        block_list.add(short_platform)
        if(random.randrange(3) == 1):
            money = Money(random.randrange(short_platform.rect.left + 20, short_platform.rect.right - 20), short_platform.rect.top - 50)
            money_list.add(money)



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


    if((player.rect.x > WALK_LIMIT_RIGHT) and (bg_move == DIRECTION_RIGHT)): 
        bg_offset -= 2
        player.control(0)
        for block in block_list:
            block.update()
        for money in money_list:
            money.update()

    if((player.rect.left <= EDGE_LEFT) and (player.direction == DIRECTION_LEFT)):
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

        for segment in range(4):
            short_platform = Short_platform(random.randrange(EDGE_RIGHT + EDGE_RIGHT / 4* segment + 100, EDGE_RIGHT + EDGE_RIGHT / 4 * (segment + 1) - 100), random.randrange(TOP_PLATFORM_HEIGHT, BOTTOM_PLATFORM_HEIGHT))
            block_list.add(short_platform)
            if(random.randrange(3) == 1):
                money = Money(random.randrange(short_platform.rect.left + 20, short_platform.rect.right - 20), short_platform.rect.top - 50)
                money_list.add(money)

                

    for collision_platform in block_list:

        if((player.rect.top <= collision_platform.rect.bottom) and (player.rect.bottom >= collision_platform.rect.bottom) and (pygame.sprite.collide_rect(player, collision_platform))):
            if(player.is_jumping == True):
                player.rect.top = collision_platform.rect.bottom
                player.move_y = 0
                player.is_jumping = False
                player.is_falling = True

        if((player.rect.bottom >= collision_platform.rect.top) and (player.rect.centery < collision_platform.rect.top - 10) and (player.rect.right > collision_platform.rect.left) and (pygame.sprite.collide_rect(player, collision_platform))):
            if(player.is_falling):
                player.move_y = 0
                player.is_falling = False
                player.rect.bottom = collision_platform.rect.top + 1
        elif(player.is_falling == False and player.rect.bottom == collision_platform.rect.top + 1):
            player.is_falling = True

        if((collision_platform.rect.left - player.rect.right >= 1) and (collision_platform.rect.left - player.rect.right <= 2) and (player.move_x != 0) and (player.rect.bottom >= collision_platform.rect.top + 2) and (player.rect.top <= collision_platform.rect.bottom)):
            player.rect.right = collision_platform.rect.left - 1
            player.move_x = 0

        if((player.rect.left - collision_platform.rect.right >= 1) and (player.rect.left - collision_platform.rect.right <= 2) and (player.move_x != 0) and (player.rect.bottom >= collision_platform.rect.top + 2) and (player.rect.top <= collision_platform.rect.bottom)):
            player.rect.left = collision_platform.rect.right + 1
            player.move_x = 0
        
    for collision_money in money_list:
        if(pygame.sprite.collide_rect(player, collision_money)):
            collision_money.kill()


    player.jump()
    player.update()



    all_sprites_list.draw(screen)
    block_list.draw(screen)
    money_list.draw(screen)
    
    pygame.display.update()
    fps.tick(player_speed)
    

pygame.quit()