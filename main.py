import pygame
import sys
import random
pygame.init()
font = pygame.font.SysFont(None, 40)

WIDTH=800
HEIGHT=600
BACKGROUND_COLOR=(0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
SPEED_Y=5
SPEED_X=50
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
CAPTION = pygame.display.set_caption('Dodge Blocks')
PLAYER=pygame.Rect(WIDTH/2,HEIGHT-50,50,50)
SCORE=0
ENEMIES=[]
NUM_ENEMY=5
for _ in range (NUM_ENEMY):
         x = random.randint(0,WIDTH-50)
         y = 0
         enemy=pygame.Rect(x,y,50,50)
         ENEMIES.append(enemy)

game_over=False
clock= pygame.time.Clock()

spawn_timer = 0
spawn_delay = 2000

# Loop
while not game_over: 
    dt=clock.tick(60)
    clock.tick(30)
    SPEED_Y = 5 + SCORE // 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT] and PLAYER.x - SPEED_X >=0:
        PLAYER.x -= SPEED_X
                     
    elif keys [pygame.K_RIGHT] and PLAYER.x + SPEED_X + PLAYER.width<=WIDTH:
        PLAYER.x += SPEED_X
    
    spawn_timer += dt        
    if spawn_timer > spawn_delay:
        x = random.randint(0, WIDTH-50)
        enemy = pygame.Rect(x, -50, 50, 50)
        ENEMIES.append(enemy)
        spawn_timer = 0

# Updating Position of Enemy
    
    for enemy in ENEMIES:
        enemy.y += SPEED_Y

        if enemy.y > HEIGHT:
            SCORE += 1
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH-50)
           
        # Collison
        if PLAYER.colliderect(enemy):
            print("Game Over")
            game_over=True 
 
          
    SCREEN.fill(BACKGROUND_COLOR)   
    score_text = font.render(f"Score: {SCORE}", True, (255,255,255))
    SCREEN.blit(score_text, (10,10))
    for enemy in ENEMIES:
        pygame.draw.rect(SCREEN,RED,enemy)    
            
    pygame.draw.rect(SCREEN,BLUE,PLAYER) 

    pygame.display.update()
          
sys.exit()    


        
