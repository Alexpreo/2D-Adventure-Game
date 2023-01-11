import pygame
from pygame.locals import *
pygame.init()

white = 255, 255, 255,
black = 0, 0, 0
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
icon = pygame.image.load()


running = True
while running:  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(white)

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)
    pygame.display.set_caption("2D Adventure Game")
    pygame.display.set_icon(icon)
    pygame.display.flip()

pygame.quit()