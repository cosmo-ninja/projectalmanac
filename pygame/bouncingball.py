import pygame
import sys
import numpy as np
import time

pygame.init()
screenWidth = 750
screenHeight = 750

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Bouncing ball")

fps = 50

r = 10
g = 9.8
h = r

# print(h)

t = 0

clock = pygame.time.Clock()
start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if h < screenHeight-r:
        t = t + (1000/(fps*1000))
        h = (0.5*g*t*t)
        print(time.time()-start_time, t)
    


    screen.fill((0,0,0))
    pygame.draw.circle(screen, center=(200, h), radius=r, color=(255,255,0))

    clock.tick(50)
    pygame.display.flip()
