import pygame

#initialise pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders Have Arrived")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
img_player = pygame.image.load("spaceship.png")
player1_x = 368#this is the middle of a 800 screen with a 64px icon
player1_y = 536#and the is the bottom of a 600

def player(x,y):
    screen.blit(img_player, (x,y))



#game loop
is_running = True
while is_running:
    #RGB
    screen.fill((144, 150, 95))
    player1_x += 0.1    #we got our icon moving
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_running = False

    player(player1_x,player1_y)
    pygame.display.update()