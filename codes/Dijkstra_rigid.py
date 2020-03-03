import numpy as np
import time
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((300,200))
gameDisplay.fill(white)

pointRobot = pygame.PixelArray(gameDisplay)
pointRobot[10][20] = green

pygame.draw.circle(gameDisplay, red, (225,50), 25)

pygame.draw.polygon(gameDisplay, red, ((25,15),(75,15),(100,50),(75,80),(50,50),(20,80)))
#pygame.draw.polygon(gameDisplay, red, ((30,95),(75,185),(100,150),(75,120),(50,150),(20,120)))
#pygame.draw.polygon(gameDisplay, red, ((225,10),(225,40),(200,15),(250,15)))

pygame.draw.ellipse(gameDisplay, red, [150, 100, 80, 40])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()