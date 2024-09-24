#infa buyalichvict24'24.09
import pygame
from pygame.draw import *
import pygame.draw
from random import randint
pygame.init()
FPS = 30
screen = pygame.display.set_mode((700, 500))
#pygame.color(0, 0, 0)
x1=349
y1=249
color = (randint(0,255), randint(0,255), randint(0,255))

ellipse(screen, color, (x1-50, y1-5, x1//5, y1//6))
polygon(screen, color, ((x1, y1), (x1+200, y1), (x1, y1+20)))
polygon(screen, color, ((x1-40-5, y1+25), (x1-70-5, y1-25), (x1-60-5, y1-25), (x1-10-5, y1)))
polygon(screen, color, ((x1+5, y1), (x1+15, y1+50), (x1-35, y1+100), (x1, y1+50), (x1-25, y1)))
polygon(screen, color, ((x1-10, y1), (x1, y1+50), (x1-50, y1+75), (x1-20, y1+50), (x1-10, y1)))
polygon(screen, color, ((x1-50, y1+10), (x1-70, y1+20), (x1-50, y1+20)))
ellipse(screen, color, (x1-120, y1-30, 50, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



#def threug():
    #line(screen, color, (x1, y1), (x1+200, y1), 3)
    #line(screen, color, (x1, y1+20), (x1+200, y1), 3)
    #line(screen, color, (x1, y1+20), (x1+200, y1), 3)
    #line(screen, color, (x1+200, y1), (x1, y1))

#circle(screen, (100, 30, 255), (200, 175), 50, 5)
#rect(screen, color, (300, 255, 100, 100), 3)
#rect(screen, color, (x1, y1, x2 - x1, y1 - y2), 3)
#line(screen, color, (x1, y1), (x2, y2), 8)

#s = pygame.Surface((x1, y1)) #pygame.SRCALPHA, 32)
#s = s.convert_alpha()

#s = pygame.transform.rotate(s, 30)
#screen.blit(s, (x1 - x1//8, y1 - y1//8))