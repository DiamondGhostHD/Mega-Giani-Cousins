import pygame

pygame.init()
pygame.font.init()


# display resolution
edge_left = 0
edge_right = 1600
edge_top = 0
edge_bottom = 900
screen = pygame.display.set_mode((edge_right, edge_bottom))


# display color
color_display = (140, 217, 7)
screen.fill(color_display)


running = True
while running:

    screen.fill(color_display)  # erease what's been before

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                running = False

    # refreshing the display
    pygame.display.update()


pygame.quit()