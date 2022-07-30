import shot
import pygame

class Spaceship:

    
    
    def __init__(self, x, y, screen):
        
        self.x = x
        self.y = y
        self.screen = screen
        self.mag = []
        self.magCounter = 0

        self.obj = pygame.image.load('pictures/spaceship.png').convert_alpha()
        self.obj = pygame.transform.scale(self.obj, ( 50, 50))
    
    def shoot(self):
        self.mag.append(shot.Shot(self.x + 8.5, self.y - 20, self.screen))
        self.magCounter += 1
