import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

RED = (195, 77, 0)
LAVANDER = (200, 200, 250)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, LAVANDER, YELLOW, MAGENTA, BLACK]

class Ball():
    def __init__(self):
        self.new()
        
    def new(self):
        self.x = randint(50, 550)
        self.y = randint(55, 550)
        self.r = randint(10,20)
        self.vx = randint(1, 10)
        self.vy = randint(1, 10)
        self.color = COLORS[randint(0, 2)]
        self.live = True

    def move(self):
        if not self.live: return
        self.x += self.vx
        self.y += self.vy
        if not (self.r < self.x < 600- self.r):
            self.vx = -self.vx
        if self.r > self.y:
            self.vy = -self.vy
            self.y = self.r
        if 600 - self.r < self.y:
            self.vy = -self.vy
            self.y = 600 - self.r
        self.vy += 1
    
    def draw(self, screen):
        circle(screen, self.color, (self.x, self.y), self.r)
    
    def test(self, pos):
        return (self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2 < self.r ** 2
    
def test_collision(b1, b2):
        return (b1.x - b2.x ) ** 2 + (b1.y - b2.y) ** 2 < (b1.r + b2.r) ** 2
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = [Ball() for _ in range(8)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                for i in range(len(balls)):
                    if balls[i].test(event.pos):
                        balls[i].live = not balls[i].live
                # for b in balls:
                #     if b.test(event.pos):
                #         b.live = False

    for b in balls:
        b.draw(screen)
        b.move()
        
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if test_collision(balls[i], balls[j]):
                balls[i].new()
                balls[j].new()
            
                
    pygame.display.update()
    screen.fill(BLACK)        

        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #if event.button == 1:
                #circle(screen, RED, event.pos, 15)
                #pygame.display.update()
            #elif event.button == 3:
                #circle(screen, BLUE, event.pos, 50)
                #pygame.display.update()

pygame.quit()