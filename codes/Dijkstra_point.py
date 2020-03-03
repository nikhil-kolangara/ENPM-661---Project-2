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

pygame.draw.circle(gameDisplay, red, (225,150), 25)

pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))

#pygame.draw.ellipse(gameDisplay, red, )

#pygame.draw.rect(gameDisplay, red, ())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

