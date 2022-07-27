import pygame

class Shot:


    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

        self.obj = pygame.image.load('pictures/laserbeam.jpg')
        self.obj = pygame.transform.scale(self.obj, (30, 30))

        self.screen.blit(self.obj, (self.x, self.y))