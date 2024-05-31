import pygame
import random

#initialise pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders Have Arrived")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player variables
img_player = pygame.image.load("spaceship.png")
player1_x = 368# this is the middle of a 800px wide screen with a 64px icon
player1_y = 536# and the is the bottom of a 600 high
player1_x_change = 0
player1_y_change = 0

#enemy variables
img_enemy = pygame.image.load("alien-ship.png")
enemy1_x = random.randint(0,736)
enemy1_y = random.randint(50,200)
enemy1_x_change = 0
#player1_y_change = 0


# player function
def player(x,y):
    screen.blit(img_player, (x,y))


# enemy function
def enemy(x,y):
    screen.blit(img_enemy, (x,y))



# game loop
is_running = True
while is_running:
    # RGB
    screen.fill((144, 150, 95))

    # event iteration
    for e in pygame.event.get():

        # closing event
        if e.type == pygame.QUIT:
            is_running = False
        # press arrow key event
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player1_x_change = -0.5
            if e.key == pygame.K_RIGHT:
                player1_x_change = 0.5
            if e.key == pygame.K_UP:
                player1_y_change = -0.5
            if e.key == pygame.K_DOWN:
                player1_y_change = 0.5

        # release key event
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                player1_x_change = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                player1_y_change = 0

    # modify location
    player1_x += player1_x_change
    player1_y += player1_y_change

    # keep inside screen boundary
    if player1_x <= 3:
        player1_x = 3
    if player1_x >= 733:    #  becos 800 - 64 for icon size
        player1_x = 733
    if player1_y <= 3:
        player1_y = 3
    if player1_y >= 536:
        player1_y = 536

    player(player1_x, player1_y)
    enemy(enemy1_x, enemy1_y)

    # update
    pygame.display.update()