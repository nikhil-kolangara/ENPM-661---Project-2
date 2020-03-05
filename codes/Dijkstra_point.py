import numpy as np
import time
import pygame
from pygame import gfxdraw

# User Input for Initial Node

print("Enter the initial position for the robot")
initialX = int(input("Enter the X point where the robot will start: "))
initialY = int(input("Enter the Y point where the robot will start: "))
goalX = int(input("Enter the X point where the robot should reach: "))
goalY = int(input("Enter the Y point where the robot should reach: "))

print("The dimension and clearance for point robot will be zero")

# Adjusting to the pygame convention of origin starting at top-left corner

initialY = 200 - initialX
goalY = 200 - goalY

# Checking if user input is within bounds

if ((initialX > 300) and (initialY > 200)):
    print("The start position of robot is out of window")
    exit(0)

if ((goalX > 300) and (goalY > 200)):
    print("The goal position of robot is out of window")
    exit(0)

startNode = [initialX, initialY]
goalNode = [goalX, goalY]

# Building the obstacle space in pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (0,255,255)

gameDisplay = pygame.display.set_mode((300,200))
gameDisplay.fill(white)

pygame.draw.circle(gameDisplay, red, (225,50), 25)

pygame.draw.polygon(gameDisplay, red, ((25,15),(75,15),(100,50),(75,80),(50,50),(20,80)))
pygame.draw.polygon(gameDisplay, red, ((95,170),(30,132.5),(35,125),(100,162.5)))
pygame.draw.polygon(gameDisplay, red, ((200,175),(225,160),(250,175),(225,190)))

pygame.draw.ellipse(gameDisplay, red, (110, 80, 80, 40))

robot = pygame.gfxdraw.pixel(gameDisplay, 80, 100, red)
path = pygame.gfxdraw.pixel(gameDisplay, 80, 100, green)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

# Functions to Check for obstacles

# Defining class to represent Graph Nodes

class graphNodes:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.cost = math.inf
        self.parent = None

# Class to define point robot properties

class pointRobot:
    def __init__(self, initialLoc, goalLoc):
        self.initialLoc = initialLoc
        self.goalLoc = goalLoc

pixelBot = pointRobot(startNode, goalNode)

class actionSet:
    def __init__(self):
        return None
    def moveUp():
        costToMove = 1
        if y > 0 and if obstacele is not there:
            newLoc = [x, y - 1]
            return costToMove and newLoc
        else return None and None

    def moveDown():

    def moveLeft():

    def moveRight():

    def moveUpRight():

    def moveUpLeft():

    def moveDownLeft():

class checkObstacle:
    def __init__(self):
        return None

    def checkCircle(point):
        increase = dimension + clearance
        center = [225, 50]
        point_x = point[0]
        point_y = point[1]
        dist = np.sqrt((point_x - center[0]) ** 2 + (point_y - center[1]) ** 2)
        if dist <= 25:
            return True
        else:
            return False

    def check_obstacle_ellipse(point, dimension, clearance):
        increase = dimension + clearance
        center = [140, 30]
        rx = 15 + increase
        ry = 6 + increase
        point_x = point[0]
        point_y = point[1]
        dist = (((point_x - center[0]) ** 2) / (rx ** 2)) + (((point_y - center[1]) ** 2) / (ry ** 2))
        if dist <= 1:
            return True
        else:
            return False




def findTotalNodes(node):
    x = node[0]
    y = node[1]
    count = 0
    if y > 0:
        count = count + 1
    if y < 200:
        count = count + 1
    if x > 0:
        count = count + 1
    if x < 300:
        count = count + 1
    if x < 300 and y > 0:
        count = count + 1
    if x > 0 and y > 0:
        count = count + 1
    if x < 300 and y < 200:
        count = count + 1
    if x > 0 and y < 200:
        count = count + 1
    return count


def solveDijkstra(robot):
    dimension = 0
    clearance = 0

    startNode = robot.startNode
    goalNode = robot.goalNode

    pygame.gfxdraw.pixel(gameDisplay, startNode[0], startNode[1], blue)
    pygame.gfxdraw.pixel(gameDisplay, goalNode[0], goalNode[1], black)

    initialNode = graphNodes(startNode)
    initialNode.cost = 0

    totalNodes = findTotalNodes(goalNode)
    print("Total number of nodes are: ", totalNodes)

    visitedNodes = []
    priorityQueue = [initialNode]
    actionList = [1, 2, 3, 4, 12, 23, 34, 14]

    iterations = 0

    while priorityQueue:
        count = 0
        currentLoc = popQ(priorityQueue)
        currentCoords = currentLoc.coordinates
        visitedNodes[count] = str(currentCoords)

        if iterations == totalNodes:
            return nextNode.parent

        for moves in actionList:
            nextCoords, actionCost = nextNode(moves, currentCoords,polyObstacle)

            if nextCoords is not None:
                if newCoords == goalNode:
                    if iterations < totalNodes:
                        iterations = iterations + 1
                        print("Robot reached the goal Node", iterations)

                nextNode = graphNodes(nextCoords)
                nextNode.parent = currentLoc

                pygame.gfxdraw.pixel(gameDisplay, startNode[0], startNode[1], yellow)
                pygame.gfxdraw.pixel(gameDisplay, goalNode[0], goalNode[1], yellow)

                if str(nextCoords) not in visitedNodes:
                    nextNode.cost = actionCost + nextNode.parent.cost
                    visited[count] = str(nextNode.coordinates)
                    priorityQueue[count] = nextNode
                else:
                    existingNodeCoords = findNExtNode(nextLoc, priorityQueue)
                    if existingNodeCoords is not None:
                        temporaryNode = priorityQueue[existingNodeCoords]
                        if temporaryNode.cost > actionCost + nextNode.parent.cost:
                            temporaryNode.cost = actionCost + nextNode.parent.cost
                            temporaryNode.parent = currentLoc
            else:
                continue
    return None, None





# Action Set Class





finalOutput = solveDijksta(pointRobot)

