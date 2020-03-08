"""
ENPM 662 : Planning for Autonomous Robotics
Project 2 : Dijkstra Algorithm for path finding and traversing for a rigid robot with Radius of robot and clearance with obstacle
Team Members : Sukoon Sarin, Nikhil Kolangra
"""
import numpy as np
import pygame
from pygame import gfxdraw
import math
import time

####################################################################################################################################################
def obstacleCheck(x, y):
    flag = 0
    # check if point is in circle shaped obstacle or not
    if ((x - 225) ** 2 + (y - 50) ** 2 - 25 ** 2) <= 0:
        flag = 1
    # check if point is in rhombus shaped obstacle or not
    if (0.6 * x + y - 325 <= 0) and (0.6 * x + y - 295 >= 0) and (y - 0.6 * x - 55 <= 0) and (y - 0.6 * x - 25 >= 0):
        flag = 1
    # check if point is in rectangle shaped obstacle or not
    if (1.72 * x + y - 333.4 <= 0) and (1.7 * x + y - 183.5 >= 0) and (y - 0.577 * x - 115.19 <= 0) and (y - 0.575 * x - 103.862 >= 0):
        flag = 1

    # check if point is in polygon shaped obstacle or not : 1st Quad
    if (y + 13 * x - 340 >= 0) and (y - 15 >= 0) and (y + x - 100 <= 0) and (y + 1.4 * x - 120 <= 0):
        flag = 1
    # check if point is in polygon shaped obstacle or not : 12nd Quad
    if (y - 1.4 * x + 90 >= 0) and (y + 1.2 * x - 170 <= 0) and (y - 1.2 * x + 10 <= 0) and (y + 1.4 * x - 120 >= 0):
        flag = 1
    # check if point is in eclipse shaped obstacle or not
    if ((x - 150) / 40) ** 2 + ((y - 100) / 20) ** 2 - 1 <= 0:
        flag = 1
    return flag

#################################################################################################################################################
# Function to Check for Obstacles
def obstacleCheck_rigid(x,y,pad):
    #Shift for rhombus
    d1=pad*math.sqrt((0.6)**2+1)
    d2=pad*math.sqrt((0.6)**2+1)
    d3=pad*math.sqrt((-0.6)**2+1)
    d4=pad*math.sqrt((-0.6)**2+1)

    #shift for rectangle

    d5=pad*math.sqrt((1.72)**2+1)
    d6=pad*math.sqrt((1.7)**2+1)
    d7=pad*math.sqrt((-0.577)**2+1)
    d8=pad*math.sqrt((-0.575)**2+1)

    #shift for Polygon part1

    d9=pad*math.sqrt((13)**2+1)
    d10=pad*math.sqrt((1)**2+1)

    #shift for Polygon part2
    d11=pad*math.sqrt((-1.4)**2+1)
    d12=pad*math.sqrt((1.2)**2+1)
    d13=pad*math.sqrt((-1.2)**2+1)

    #partition
    d14=pad*math.sqrt((1.4)**2+1)
    d15=pad*math.sqrt((1.4)**2+1)

    flag = False
    if (x < pad) or (x > 300-pad) or (y < pad) or (y > 200-pad):
        flag = True

    #check if point is in circle shaped obstacle or not

    if ((x - 225)**2 + (y-50)**2 - (25+pad)**2) <= 0:
        flag = True

    #check if point is in rhombus shaped obstacle or not

    if (0.6 * x + y - 325 - d1 <= 0) and (0.6 * x + y - 295 + d2 >= 0) and (y - 0.6 * x - 55 - d3 <= 0) and (y - 0.6 * x - 25 + d4 >= 0):
        flag = True

    #check if point is in rectangle shaped obstacle or not
    if (1.72 * x + y - 333.4 - d5 <= 0) and (1.7 * x + y - 183.5 + d6 >= 0) and (y - 0.577 * x - 115.19 - d7 <= 0) and (y - 0.575 * x - 103.862 + d8 >= 0):
        flag = True

    #check if point is in polygon shaped obstacle or not : 1st Quad
    if (y + 13 * x - 340 + d9 >= 0) and (y - (15-pad) >= 0) and (y + x - 100 - d10 <= 0) and (y + 1.4 * x - 120 - d14 <= 0):
        flag = True

    #check if point is in polygon shaped obstacle or not : 12nd Quad
    if (y - 1.4 * x + 90 + d11 >= 0) and (y + 1.2 * x - 170 - d12 <= 0) and (y - 1.2 * x + 10 - d13 <= 0) and (y + 1.4*x - 120 + d15 >= 0):
        flag = True

    #check if point is in eclipse shaped obstacle or not
    if ((x-150)/(40+pad))**2 + ((y-100)/(20+pad))**2 - 1 <=0:
        flag = True

    return flag
######################################################################################################################################################
# Defining class to represent Graph Nodes

class graphNodes:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.cost = math.inf #Starting With High Cost Values
        self.parent = None

# Class to define point robot properties

class pointRobot:
    def __init__(self, initialLoc, goalLoc):
        self.initialLoc = initialLoc
        self.goalLoc = goalLoc

######################################################################################################################################################
#To give the least cost nodes

def popQ(priorityQueue):
    minCost = 0
    for item in range(len(priorityQueue)):
        if priorityQueue[item].cost < priorityQueue[minCost].cost:
            minCost = item
    return priorityQueue.pop(minCost)

def getNode(coordinates, priorityQueue):
    for items in priorityQueue:
        if items.coordinates == coordinates:
            return priorityQueue.index(items)
        else:
            return None

def moveUp(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    if yCoord > 0 and not(obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def moveDown(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1

    if yCoord < 200 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord, yCoord + 1]
        return costToMove, newLoc
    else:
        return None, None

def moveLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1

    if xCoord > 0 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord - 1, yCoord]
        return costToMove, newLoc
    else:
        return None, None

def moveRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    #ck = checkObstacle(xCoord, yCoord)
    if xCoord < 300 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord + 1, yCoord]
        return costToMove, newLoc
    else:
        return None, None

def moveUpRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    #ck = checkObstacle(xCoord, yCoord)
    if yCoord > 0 and xCoord < 300 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord + 1, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def moveUpLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    #ck = checkObstacle(xCoord, yCoord)
    if yCoord > 0 and xCoord > 0 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord - 1 , yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def moveDownLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    #ck = checkObstacle(xCoord, yCoord)
    if yCoord < 200 and xCoord > 0 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord - 1, yCoord + 1]
        return costToMove, newLoc
    else:
        return None, None

def moveDownRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    #ck = checkObstacle(xCoord, yCoord)
    if yCoord< 200 and xCoord < 300 and not (obstacleCheck_rigid(xCoord, yCoord,pad)):
        newLoc = [xCoord, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def updateGameDisplay(gameDisplay, coordinates, yellow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # +quit()
    pygame.gfxdraw.pixel(gameDisplay, coordinates[0], coordinates[1], yellow)
            
    pygame.display.update()

def updateNodeLoc(action, coordinates):
    if action == 1:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUp(coordinates)
    if action == 2:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveRight(coordinates)
    if action == 3:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDown(coordinates)
    if action == 4:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveLeft(coordinates)
    if action == 12:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUpRight(coordinates)
    if action == 23:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDownRight(coordinates)
    if action == 34:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDownLeft(coordinates)
    if action == 14:
        #updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUpLeft(coordinates)

def findTotalNodes(coordinates):
    x = coordinates[0]
    y = coordinates[1]
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
#########################################################################################################################################
def solveDijkstra(pixelBot):

    startLoc = pixelBot.initialLoc
    goalLoc = pixelBot.goalLoc

    pygame.gfxdraw.pixel(gameDisplay, startNode[0], startNode[1], blue)
    pygame.display.update()
    pygame.gfxdraw.pixel(gameDisplay, goalNode[0], goalNode[1], green)
    pygame.display.update()
    
    initialNode = graphNodes(startLoc)
    initialNode.cost = 0

    totalNodes = findTotalNodes(goalLoc)

    visitedNodes = []
    priorityQueue = [initialNode]
    actionList = [1, 2, 3, 4, 12, 23, 34, 14]
    visitedNodes_list = []
    iterations = 0

    while priorityQueue:
        currentLoc = popQ(priorityQueue)
        currentCoords = currentLoc.coordinates
        visitedNodes.append(str(currentCoords))
        visitedNodes_list.append(currentCoords)
        if iterations == totalNodes:
            return nextNode.parent

        for moves in actionList:
            actionCost, nextCoords = updateNodeLoc(moves, currentCoords)

            if nextCoords is not None:
                if nextCoords == goalLoc:
                    if iterations < totalNodes:
                        iterations = iterations + 1


                nextNode = graphNodes(nextCoords)
                nextNode.parent = currentLoc
                if str(nextCoords) not in visitedNodes:
                    nextNode.cost = actionCost + nextNode.parent.cost
                    visitedNodes.append(str(nextNode.coordinates))
                    visitedNodes_list.append((nextNode.coordinates))
                    #print("vis",nextNode.coordinates[0], nextNode.coordinates[1])
                    # for event in pygame.event.get():
                    #     if event.type == pygame.QUIT:
                    #         pygame.quit()
                    #         quit()
                    # for i in range(len(visitedNodes)):

                    pygame.gfxdraw.pixel(gameDisplay, nextNode.coordinates[0], nextNode.coordinates[1], (255,255,0))
                    pygame.display.update()
                    priorityQueue.append(nextNode)
                else:
                    existingNodeCoords = getNode(nextCoords, priorityQueue)
                    if existingNodeCoords is not None:
                        temporaryNode = priorityQueue[existingNodeCoords]
                        if temporaryNode.cost > actionCost + nextNode.parent.cost:
                            temporaryNode.cost = actionCost + nextNode.parent.cost
                            temporaryNode.parent = currentLoc
            else:
                continue
    return None

def backTrack(node):
    backTrackList = []
    backTrackList.append(node.parent)
    parent = node.parent
    if parent == None:
        return backTrackList
    while parent is not None:
        backTrackList.append(parent)
        parent = parent.parent
        if(parent == None):
            break
    finalTrackedPath = backTrackList.copy()
    return finalTrackedPath

###########################################################################################################################################
# User Input for Initial Node

print("Enter the initial position for the robot")
initialX = int(input("Enter the X point where the robot will start: "))
initialY = int(input("Enter the Y point where the robot will start: "))
goalX = int(input("Enter the X point where the robot should reach: "))
goalY = int(input("Enter the Y point where the robot should reach: "))

# Adjusting to the pygame convention of origin starting at top-left corner

initialY = 200 - initialY
goalY = 200 - goalY

print("Enter the size of robot")

size = int(input())

print("Enter the clearance")
clearance = int(input())

pad = size + clearance

# Checking if user input is within bounds

if initialX > 300 or initialY > 200 or initialX < 0 or initialY < 0 or obstacleCheck_rigid(initialX, initialY,pad):
    print("The start position of robot is out of window or within the obstacle")
    exit(0)

if goalX > 300  or goalY > 200 or goalX < 0 or goalY < 0 or obstacleCheck_rigid(goalX, goalY, pad):
    print("The goal position of robot is out of window or within the obstacle")
    exit(0)


startNode = [initialX, initialY]
goalNode = [goalX, goalY]

pixelBot = pointRobot(startNode, goalNode)

# Building the obstacle space in pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (0,255,255)

gameDisplay = pygame.display.set_mode((300,200))
gameDisplay.fill(black)

pygame.draw.circle(gameDisplay, red, (225,50), 25)
#Drawing Polygon
pygame.draw.polygon(gameDisplay, red, ((25,15),(75,15),(100,50),(75,80),(50,50),(20,80)))
#Drawing Rectangle
pygame.draw.polygon(gameDisplay, red, ((95,170),(30,132.5),(35,124),(100,161.4)))
#Drawing Rhombus
pygame.draw.polygon(gameDisplay, red, ((200,175),(225,160),(250,175),(225,190)))

pygame.draw.ellipse(gameDisplay, red, (110, 80, 80, 40))

#robot = pygame.gfxdraw.pixel(gameDisplay, 80, 100, red)

start_time = time.time()
print("Exploring Nodes")
finalOutput = solveDijkstra(pixelBot)
print("GOAL REACHED")
if finalOutput is not None:
    tracedPath = backTrack(finalOutput)
    print("Starting Back Tracking")
    for items in tracedPath:
        x1 = items.coordinates[0]
        y1 = items.coordinates[1]
        
        gfxdraw.pixel(gameDisplay, x1, y1, blue)
        pygame.display.update()
end_time = time.time()
total_time = end_time-start_time
print("Total Execution Time:",total_time)

while  True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
     pass


