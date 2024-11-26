import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (155, 77, 0)
BLUE = (0, 200, 250)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 15)
                pygame.display.update()
            elif event.button == 3:
                circle(screen, BLUE, event.pos, 50)
                pygame.display.update()

pygame.quit()