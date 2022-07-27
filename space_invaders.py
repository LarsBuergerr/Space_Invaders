from math import fabs
from random import *
import sys
from threading import Timer
from time import sleep
from spaceship import *
from invader import *
from pygame import *

if __name__ == "__main__":

    init()
    flags = DOUBLEBUF
    screen = display.set_mode((800,600), flags, 16)
    screen.set_alpha(None)
    # Title
    display.set_caption("pictures/space_invaders")
    isRunning = 1
    #Loading image
    event.set_allowed([QUIT, KEYDOWN, KEYUP])

    player = Spaceship(375, 500, screen)

    #Specifying the X and Y Coordinates
    Xchange = 0
    Ychange = 0
    lastShot = 0
    currShot = 0
    lastWave = 0
    currWave = 0
    waveCount = 1
    invSpeed = 0.005
    invaders = []

    print(len(invaders))
    while(isRunning):
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                isRunning = 0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Ychange-=0.4
                if(event.key == K_DOWN):
                    Ychange+=0.4
                if event.key == K_LEFT:
                    Xchange-=0.4
                if event.key == K_RIGHT:
                    Xchange+=0.4
                if event.key == K_SPACE:
                    currShot = time.get_ticks()
                    if(currShot - lastShot > 200):
                        player.shoot()
                        lastShot = time.get_ticks()

            currWave = time.get_ticks()
            if(currWave - lastWave > 5000):
                for i in range(waveCount):
                    invaders.append(Invader(randint(0, 700), randint(0, 200), screen))
                lastWave = time.get_ticks()  
                waveCount += 1  
                invSpeed += 0.008
                
            if event.type == KEYUP:
                Ychange=0
                Xchange=0
        if player.x+Xchange>775 or player.y+Ychange>565 or player.x+Xchange<0 or player.y+Ychange<0:
            player.y+=0
            player.x+=0
        else:
            player.y+=Ychange
            player.x+=Xchange
        screen.blit(player.obj,(player.x, player.y))

        for s in player.mag:
            if s.x>780 or s.y>585 or s.x<0 or s.y<0:
                player.mag.remove(s)
            else:
                s.y -= 0.3
            screen.blit(s.obj, (s.x, s.y))

        for inv in invaders:
            if(inv.movement == 0):
                inv.x -= 0.2
                if(inv.x < 3):
                    inv.movement = 1   
            else:
                inv.x += 0.2
                if(inv.x > 770):
                    inv.movement = 0
            inv.y += invSpeed
            screen.blit(inv.obj, (inv.x, inv.y))
            for s in player.mag:
                if(fabs(s.x - 7 - inv.x) < 25 and fabs(s.y - inv.y) < 20):
                    invaders.remove(inv)
                    player.mag.remove(s)
            
            if(fabs(player.x - 7 - inv.x) < 25 and fabs(player.y - inv.y) < 20 or inv.y > 600):
                screen.fill((0, 0, 0))
                sys.exit()



        #for i in range(len(shotArr)):
        #    print(len(shotArr))
        #    if(shotArr[i] is not None):
        #        print(shotX)
        #        print(shotY)
        #        screen.blit(shotArr[i], (shotX,  shotY + 0.3))
        display.update()