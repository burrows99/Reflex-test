import pygame
import random
pygame.init()
screenwidth=1500
win=pygame.display.set_mode((screenwidth,screenwidth-800))
pygame.display.set_caption("Reflex test")

score=0
counter=0

x=50
y=50

x1=750
y1=350

width=75
height=75

width1=5
height1=5

velocity=4
velocity1=.08

run=True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>velocity:
        x-=velocity
    if keys[pygame.K_RIGHT] and x<screenwidth-width-velocity:
        x+=velocity
    if keys[pygame.K_UP] and y>velocity:
        y-=velocity
    if keys[pygame.K_DOWN] and y<screenwidth-800-height-velocity:
        y+=velocity

    for i in range(100):
        a1=random.randint(1,4)
        if a1==1 and x1>velocity1 :
            for u in range(15):
                x1=x1-velocity1
        if a1==2 and x1<screenwidth-width1-velocity1:
            for u in range(15):
                x1=x1+velocity1
        if a1==3 and y1>velocity1:
            for u in range(15):
                y1=y1-velocity1
        if a1==4 and y1<screenwidth-800-height1-velocity1:
            for u in range(15):
                y1=y1+velocity1

    if keys[pygame.K_SPACE]:
        counter=counter+1

    if x1>=x and x1<=x+75 and y1>=y and y1<=y+75 and keys[pygame.K_SPACE]:
        score=score+1
        
    win.fill((0,0,0))

    pygame.draw.rect(win,(255,0,0),(x,y,width,height),2)
    pygame.draw.rect(win,(0,255,0),(x1,y1,width1,height1))
    pygame.display.update()
    
print(str(int((float(score)/float(counter))*float(100)))+'%')
    
pygame.quit()
