import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
PLAYER_BOTTOM = 75
PLAYER_SPEED = 0.1
OBJECT_WIDTH = 50
OBJECT_HEIGHT = 50
OBJECT_SPEED = 0.1
OBJECTS_DISTANCE = 200
ACTUAL_HEIGHT = SCREEN_HEIGHT - PLAYER_BOTTOM - PLAYER_HEIGHT

playerX = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
running = True
goingLeft = False
goingRight = False
directionPriority = ""
timeForNewObject = time.time()
print(timeForNewObject)

class Object:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

objects = []
print(ACTUAL_HEIGHT / (OBJECTS_DISTANCE+OBJECT_HEIGHT))
for i in range(0, 4):
    type = random.randint(0, 2)
    if type == 0:
        type = "bomb"
    elif type == 1:
        type = "trash"
    else:
        type = "fruit"
    objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECTS_DISTANCE*i - OBJECT_HEIGHT, type))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                goingLeft = True
                directionPriority = "left"
            elif event.key == pygame.K_RIGHT:
                goingRight = True
                directionPriority = "right"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                goingLeft = False
                directionPriority = "right"
            elif event.key == pygame.K_RIGHT:
                goingRight = False
                directionPriority = "left"
    if directionPriority == "left":
        if goingLeft:
            playerX -= PLAYER_SPEED
        elif goingRight:
            playerX += PLAYER_SPEED
    elif directionPriority == "right":
        if goingRight:
            playerX += PLAYER_SPEED
        elif goingLeft:
            playerX -= PLAYER_SPEED
    
    SCREEN.fill((0, 0, 0))

    for object in objects:
        if object.type == "bomb":
            pygame.draw.rect(SCREEN, (255, 0, 0), (object.x, object.y, OBJECT_WIDTH, OBJECT_HEIGHT))
        elif object.type == "trash":
            pygame.draw.rect(SCREEN, (255, 255, 255), (object.x, object.y, OBJECT_WIDTH, OBJECT_HEIGHT))
        else:
            pygame.draw.rect(SCREEN, (0, 255, 0), (object.x, object.y, OBJECT_WIDTH, OBJECT_HEIGHT))
        object.y += OBJECT_SPEED
        
        if object.y >= SCREEN_HEIGHT:
            objects.remove(object)
            type = random.randint(0, 2)
            if type == 0:
                type = "bomb"
            elif type == 1:
                type = "trash"
            else:
                type = "fruit"
            objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT, type))

    
    
    pygame.draw.rect(SCREEN, (255, 0, 0), (playerX, SCREEN_HEIGHT-PLAYER_HEIGHT-PLAYER_BOTTOM, 50, 75))
    pygame.display.update()