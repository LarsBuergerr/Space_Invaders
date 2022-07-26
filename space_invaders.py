import pygame

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)

# Initialise the pygame functions#
pygame.init()

# Create the screen for the user#
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load("space.png")
#pygame.display.set_icon(icon)

x    = 20
y    = 20
rect = pygame.draw.rect(screen, WHITE,(x, y, 50, 50))

# Makes the pygame window appear for longer than a few milliseconds#
runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_a):
                print("a")
                rect.x -= 5 
            if(event.key == pygame.K_s):
                rect.y -= 5
            if(event.key == pygame.K_d):
                rect.x += 5
            if(event.key == pygame.K_w):
                rect.x += 5

    pygame.display.update()


