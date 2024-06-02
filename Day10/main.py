import math

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
background = pygame.image.load("space.jpg")

# PLAYER variables
img_player = pygame.image.load("spaceship.png")
player1_x = 368# this is the middle of a 800px wide screen with a 64px icon
player1_y = 500# and 536 is the bottom of a 600 high, 500 for aesthetics
player1_x_change = 0
player1_y_change = 0

# ENEMY variables
img_enemy = []
enemy1_x = []
enemy1_y = []
enemy1_x_change = []
enemy1_y_change = []
number_of_enemies = 8

for ene in range(number_of_enemies):
    img_enemy.append(pygame.image.load("alien-ship.png"))
    enemy1_x.append(random.randint(0,736))
    enemy1_y.append(random.randint(50,200))
    enemy1_x_change.append(.5)
    enemy1_y_change.append(40)


# BULLET variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 2.5
visible_bullet = False

# SCORE
score = 0

# PLAYER function
def player(x,y):
    screen.blit(img_player, (x,y))


# ENEMY function
def enemy(x,y, en):
    screen.blit(img_enemy[en], (x,y))

# SHOOT function
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x +16,y +10))

def there_is_a_collision(x_1, y_1,x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance< 27:
        return True
    else:
        return False


# GAME LOOP
is_running = True
while is_running:
    # background image
    screen.blit(background, (0,0))

    # event iteration
    for e in pygame.event.get():

        # CLOSING event
        if e.type == pygame.QUIT:
            is_running = False
        # PRESS key event
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player1_x_change = -1
            if e.key == pygame.K_RIGHT:
                player1_x_change = 1
            if e.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x = player1_x
                    shoot_bullet(bullet_x, bullet_y)


        # RELEASE key event
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                player1_x_change = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                player1_y_change = 0

    # MODIFY player location
    player1_x += player1_x_change
    #player1_y += player1_y_change

    # keep player inside screen boundary
    if player1_x <= 3:
        player1_x = 3
    if player1_x >= 733:    #  becos 800 - 64 for icon size
        player1_x = 733
    if player1_y <= 3:
        player1_y = 3
    if player1_y >= 536:
        player1_y = 536

    # modify enemy location
    for ene in range(number_of_enemies):
        enemy1_x[ene] += enemy1_x_change[ene]

        # keep enemy inside screen boundary
        if enemy1_x[ene] <= 0:
            enemy1_x_change[ene] = .4
            enemy1_y[ene] += enemy1_y_change[ene]
        if enemy1_x[ene] >= 733:  # becos 800 - 64 for icon size
            enemy1_x_change[ene] = -.4
            enemy1_y[ene] += enemy1_y_change[ene]

        # COLLISION
        collision = there_is_a_collision(enemy1_x[ene], enemy1_y[ene], bullet_x, bullet_y)
        if collision:
            bullet_y = 500
            visible_bullet = False
            score += 1
            print(score)
            enemy1_x[ene] = random.randint(0, 736)
            enemy1_y[ene] = random.randint(50, 200)

        enemy(enemy1_x[ene], enemy1_y[ene], ene)

    # BULLETS movement
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change



    player(player1_x, player1_y)


    # update
    pygame.display.update()