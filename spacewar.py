import pygame
import random
import math
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,600))

#background=pygame.image.load("spaceship.png")
mixer.music.load("background.mp3")
mixer.music.play(-1)
pygame.display.set_caption("space hustle")
icon=pygame.image.load("gun.png")
pygame.display.set_icon(icon)

#LOADING PLYER
playerImg=pygame.image.load("spaceship.png")
playerX=370
playerY=480
playerX_change=0


enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemy=6


for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bullet_state="ready"
bulletY_change=3
bulletX_change=0

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

#DRAWING PLAYER
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,j):
    screen.blit(enemyImg[j],(x,y))    

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def show_score(x,y):
    score=font.render("score  :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    
#GAME LOOP
    
running=True
while running:
    
    #SCREEN COLOUR
    screen.fill((0,0,0))

 #   screen.blit(background(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()                       
            running=False
    #key pressing
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            playerX_change=-0.5
        if event.key==pygame.K_RIGHT:
            playerX_change=0.5
        if event.key==pygame.K_UP:
            if bullet_state is "ready":
                bulletX=playerX
               # bulletSound=mixer.Sound("bullet.mp3")
                #bulletSound.play()
                fire_bullet(playerX,bulletY)
                
            
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            playerX_change=0
                                    
    if bulletY<=0:
        bullrtY=480
        bullet_state="ready"

                
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

   
    for j in range(num_of_enemy):

        if enemyY[j]>440:
            for k in range(num_of_enemy):
                enemy[j]=2000
            game_over_text()
            break
        
        enemyX[j]+=enemyX_change[j]
        if enemyX[j]<=0:
            enemyX_change[j]=0.5
            enemyY[j]+=enemyY_change[j]
        elif enemyX[j]>=736:
            enemyX_change[j]=-0.5
            enemyY[j]+=enemyY_change[j]
            
        collision=iscollision(enemyX[j],enemyY[j],bulletX,bulletY)
        if collision:
           # collision_sound=mixer.Sound("collision.mp3")
            #collision_sound.play()
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[j]=random.randint(0,735)
            enemyY[j]=random.randint(0,150)
         
        enemy(enemyX[j],enemyY[j],j)
    
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    
    
    player(playerX,playerY)
    show_score(textY,textX)
    pygame.display.update()
    
