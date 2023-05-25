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

score = 0

playerX = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
running = True
goingLeft = False
goingRight = False
directionPriority = ""
playerImage = pygame.image.load("opened.png")

class Object:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if type == "bomb":
            self.color = (100, 100, 100)
        elif type == "trash":
            self.color = (255, 100, 0)
        else:
            self.color = (0, 255, 0)

armState = "opened"
armStateTimestamp = time.time()

def checkCollision(object):
    if playerX < object.x + OBJECT_WIDTH and playerX + PLAYER_WIDTH > object.x and SCREEN_HEIGHT - PLAYER_BOTTOM - PLAYER_HEIGHT < object.y + OBJECT_HEIGHT and SCREEN_HEIGHT - PLAYER_BOTTOM > object.y:
        return True
    else:
        return False

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
            elif event.key == pygame.K_DOWN:
                armState = "closed"
                playerImage = pygame.image.load("closed.png")
                armStateTimestamp = time.time()
            elif event.key == pygame.K_UP:
                armState = "fire"
                playerImage = pygame.image.load("fire.png")
                armStateTimestamp = time.time()
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
    
    if time.time() > armStateTimestamp + 1:
        armState = "opened"
        playerImage = pygame.image.load("opened.png")

    SCREEN.fill((0, 0, 0))

    for object in objects:
        pygame.draw.rect(SCREEN, object.color, (object.x, object.y, OBJECT_WIDTH, OBJECT_HEIGHT))
        object.y += OBJECT_SPEED
        
        if checkCollision(object):
            if object.type == "trash":
                if armState == "fire":
                    type = random.randint(0, 2)
                    if type == 0:
                        type = "bomb"
                    elif type == 1:
                       type = "trash"
                    else:
                       type = "fruit"
                    objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT - (SCREEN_HEIGHT-object.y), type))
                    objects.remove(object)
                    score += 2
                else:
                    score -= 1
            elif object.type == "bomb":
                running = False
            else:
                if armState == "closed":
                    type = random.randint(0, 2)
                    if type == 0:
                        type = "bomb"
                    elif type == 1:
                       type = "trash"
                    else:
                       type = "fruit"
                    objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT - (SCREEN_HEIGHT-object.y), type))
                    objects.remove(object)
                    score += 2
                else:
                    score -= 1
          #  objects.remove(object)
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

    
    SCREEN.blit(playerImage, (playerX, SCREEN_HEIGHT-PLAYER_HEIGHT-PLAYER_BOTTOM))
   # pygame.draw.rect(SCREEN, (255, 0, 0), (playerX, SCREEN_HEIGHT-PLAYER_HEIGHT-PLAYER_BOTTOM, 50, 75))
    pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM))
    pygame.display.update()
    print(score)