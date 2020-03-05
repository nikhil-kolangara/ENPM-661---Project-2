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
pygame.draw.polygon(gameDisplay, red, ((95,170),(30,132.5),(35,125),(100,162.5)))
pygame.draw.polygon(gameDisplay, red, ((200,175),(225,160),(250,175),(225,190)))


pygame.draw.ellipse(gameDisplay, red, (110, 80, 80, 40))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
