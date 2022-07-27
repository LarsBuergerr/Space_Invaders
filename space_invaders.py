import math
from random import *
from threading import Timer
from time import sleep
from spaceship import *
from invader import *
import pygame

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    # Title
    pygame.display.set_caption("pictures/space_invaders")
    isRunning = True
    #Loading image
    player = Spaceship(375, 500, screen)

    invader = Invader(375, 200, screen)
    
    #Specifying the X and Y Coordinates
    Xchange = 0
    Ychange = 0
    lastShot = 0
    currShot = 0
    invaders = []
    invaders.append(invader)

    print(len(invaders))
    while(isRunning ==True):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Ychange-=0.3
                if(event.key == pygame.K_DOWN):
                    Ychange+=0.3
                if event.key == pygame.K_LEFT:
                    Xchange-=0.3
                if event.key == pygame.K_RIGHT:
                    Xchange+=0.3
                if event.key == pygame.K_SPACE:
                    currShot = pygame.time.get_ticks()
                    if(currShot - lastShot > 500):
                        player.shoot()
                        lastShot = pygame.time.get_ticks()
                if event.key == pygame.K_c:
                    invaders.append(Invader(randint(0, 700), randint(0, 400), screen))


            if event.type == pygame.KEYUP:
                Ychange=0
                Xchange=0
        if player.x+Xchange>775 or player.y+Ychange>565 or player.x+Xchange<0 or player.y+Ychange<0:
            player.y+=0
            player.x+=0
        else:
            player.y+=Ychange
            player.x+=Xchange
        screen.blit(player.obj,(player.x, player.y))

        for i in player.mag:
            if i.x>780 or i.y>585 or i.x<0 or i.y<0:
                player.mag.remove(i)
            else:
                i.y -= 0.3
            screen.blit(i.obj, (i.x, i.y))

        for inv in invaders:
            screen.blit(inv.obj, (inv.x, inv.y))
            for s in player.mag:
                if(math.fabs(s.x - 7 - inv.x) < 25 and math.fabs(s.y - inv.y) < 20):
                    invaders.remove(inv)
                    player.mag.remove(s)


        #for i in range(len(shotArr)):
        #    print(len(shotArr))
        #    if(shotArr[i] is not None):
        #        print(shotX)
        #        print(shotY)
        #        screen.blit(shotArr[i], (shotX,  shotY + 0.3))
        pygame.display.update()