from random import *
import pygame


class Invader:

    def __init__(self, x, y, screen):

        self.x = x
        self.y = y
        self.movement = randint(0, 1)
        self.screen = screen
        
        self.obj = pygame.image.load('pictures/invader.png')
        self.obj = pygame.transform.scale(self.obj, (50, 50))

        self.screen.blit(self.obj, (self.x, self.y))
