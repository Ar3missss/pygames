import pygame
import sys
import random
pygame.init()

WIDTH=800
HEIGHT=600
BACKGROUND_COLOR=(0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
PLAYER=pygame.Rect(WIDTH/2,HEIGHT-50,50,50)
ENEMY=pygame.Rect(random.randint(0,WIDTH-50),0,50,50)

game_over=False
clock= pygame.time.Clock()

while not game_over: 
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER.x -= 50 
                     
            elif event.key ==pygame.K_RIGHT:
                PLAYER.x += 50

    ENEMY.y +=5
    if ENEMY.y>HEIGHT:
        ENEMY.y = 0
        ENEMY.x = random.randint(0,WIDTH-50)               


    SCREEN.fill(BACKGROUND_COLOR)       
    pygame.draw.rect(SCREEN,RED,ENEMY)        
    pygame.draw.rect(SCREEN,BLUE,PLAYER) 

          

    pygame.display.update()
        
