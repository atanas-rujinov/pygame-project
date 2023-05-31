import pygame
from pygame import mixer
import random
import time
import re

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 100)

mixer.init()
mixer.set_num_channels(2)
mixer.Channel(0).play(mixer.Sound("Among Us Drip Theme Song Original (Among Us Trap Remix Amogus Meme Music) by Leonz.mp3"), -1)
mixer.Channel(0).set_volume(1)
mixer.Channel(1).set_volume(5)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
PLAYER_BOTTOM = 75
PLAYER_SPEED = 100
OBJECT_WIDTH = 50
OBJECT_HEIGHT = 50
OBJECTS_DISTANCE = 200
ACTUAL_HEIGHT = SCREEN_HEIGHT - PLAYER_BOTTOM - PLAYER_HEIGHT

FPS = 60

objectSpeed = 3
clock = pygame.time.Clock()

score = 0
scoreLastStep = 0

textSurface = font.render(str(score), False, (0, 0, 0))

playerX = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
running = True
goingLeft = False
goingRight = False
directionPriority = ""
playerImage = pygame.image.load("opened.png")
bombImage = pygame.image.load("bomb.png")
trashImage = pygame.image.load("trash.png")
fruitImage = pygame.image.load("fruit.png")

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
    if playerX < object.x + OBJECT_WIDTH and playerX + PLAYER_WIDTH > object.x and SCREEN_HEIGHT - PLAYER_BOTTOM - PLAYER_HEIGHT < object.y + OBJECT_HEIGHT and SCREEN_HEIGHT - PLAYER_BOTTOM - 44 > object.y + OBJECT_HEIGHT:
        return True
    else:
        return False
    

def extract_username_and_score(string):
    pattern = r"^([\w\s]+)\s+(\d+)$"
    match = re.match(pattern, string)
    
    if match:
        username = match.group(1)
        score = int(match.group(2))
        return username, score
    else:
        return None

while True:

    
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 75
    PLAYER_BOTTOM = 75
    PLAYER_SPEED = 3
    OBJECT_WIDTH = 50
    OBJECT_HEIGHT = 50
    OBJECTS_DISTANCE = 200
    ACTUAL_HEIGHT = SCREEN_HEIGHT - PLAYER_BOTTOM - PLAYER_HEIGHT

    FPS = 60

    objectSpeed = 3
    clock = pygame.time.Clock()

    score = 0
    scoreLastStep = 0

    textSurface = font.render(str(score), False, (0, 0, 0))

    playerX = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
    running = True
    goingLeft = False
    goingRight = False
    directionPriority = ""
    playerImage = pygame.image.load("opened.png")
    bombImage = pygame.image.load("bomb.png")
    trashImage = pygame.image.load("trash.png")
    fruitImage = pygame.image.load("fruit.png")
    background = pygame.image.load("background.jpeg")


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

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
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
                playerX -= PLAYER_SPEED * clock.get_fps()  / FPS
            elif goingRight:
                playerX += PLAYER_SPEED * clock.get_fps()  / FPS
        elif directionPriority == "right":
            if goingRight:
                playerX += PLAYER_SPEED * clock.get_fps()  / FPS
            elif goingLeft:
                playerX -= PLAYER_SPEED * clock.get_fps()  / FPS
        if playerX < 0:
            playerX = 0
        if playerX > SCREEN_WIDTH - PLAYER_WIDTH:
            playerX = SCREEN_WIDTH - PLAYER_WIDTH
        
        if time.time() > armStateTimestamp + 1:
            armState = "opened"
            playerImage = pygame.image.load("opened.png")

        SCREEN.blit(background, (0, 0))

        for object in objects:
            if object.type == "bomb":
                SCREEN.blit(bombImage, (object.x, object.y))
            elif object.type == "trash":
                SCREEN.blit(trashImage, (object.x, object.y))
            else:
                SCREEN.blit(fruitImage, (object.x, object.y))

            object.y += objectSpeed * clock.get_fps()  / FPS
            
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
                    elif armState == "closed":
                        type = random.randint(0, 2)
                        if type == 0:
                            type = "bomb"
                        elif type == 1:
                            type = "trash"
                        else:
                            type = "fruit"
                        objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT - (SCREEN_HEIGHT-object.y), type))
                        objects.remove(object)
                        score -= 2
                elif object.type == "bomb":
                    mixer.Channel(1).play(mixer.Sound("Vine boom sound effect [TubeRipper.com].mp3"))
                    running = False
                else:
                    if armState == "closed":
                        mixer.Channel(1).play(mixer.Sound("Eating sound effect LUCAS ARPON TV [TubeRipper.com].mp3"))
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
                    elif armState == "fire":
                        type = random.randint(0, 2)
                        if type == 0:
                            type = "bomb"
                        elif type == 1:
                            type = "trash"
                        else:
                            type = "fruit"
                        objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT - (SCREEN_HEIGHT-object.y), type))
                        objects.remove(object)
                        score -= 2
            #  objects.remove(object)
            if object.y >= SCREEN_HEIGHT:
                if object.type == "fruit" or object.type == "trash":
                    score -= 1
                objects.remove(object)
                type = random.randint(0, 2)
                if type == 0:
                    type = "bomb"
                elif type == 1:
                    type = "trash"
                else:
                    type = "fruit"
                objects.append(Object(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0 - OBJECT_HEIGHT, type))
        
        if score < 0:
            score = 0
        
        if score > scoreLastStep+3:
            objectSpeed += 1
            PLAYER_SPEED += 1
            scoreLastStep = score
        
        SCREEN.blit(playerImage, (playerX, SCREEN_HEIGHT-PLAYER_HEIGHT-PLAYER_BOTTOM))
        pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
        textSurface = font.render("Score: " + str(score), True, (0, 0, 0))
        SCREEN.blit(textSurface, (5, SCREEN_HEIGHT-PLAYER_BOTTOM-10))
        pygame.display.update()
        print(score)
        print(clock.get_fps())
        clock.tick(60)

    #print("Game over! Your score is: " + str(score) + "Enter your name:")
    pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
    textSurface = font.render("Game over!", True, (0, 0, 0))
    SCREEN.blit(textSurface, (5, SCREEN_HEIGHT-PLAYER_BOTTOM-10))
    pygame.display.update()
    time.sleep(1)
    pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
    textSurface = font.render("Score: " + str(score), True, (0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
    textSurface = font.render("Enter your name:", True, (0, 0, 0))
    SCREEN.blit(textSurface, (5, SCREEN_HEIGHT-PLAYER_BOTTOM-10))
    pygame.display.update()
    name = "Enter your name:"
    startedToType = False
    typing = True
    anon = False
    while typing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if startedToType == False:
                        anon = True
                    typing = False
                if startedToType == False:
                    name = event.unicode
                    startedToType = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
        textSurface = font.render(name, True, (0, 0, 0))
        SCREEN.blit(textSurface, (5, SCREEN_HEIGHT-PLAYER_BOTTOM-10))
        pygame.display.update()

    write_newline = True

    if anon == False:
        write_newline = True  # Initialize the write_newline flag to True

        with open("scores.txt", "r") as file:
            lines = file.readlines()
            modified_lines = []  # Store the modified lines here

            for line in lines:
                result = extract_username_and_score(line)
                if result:
                    username, current_score = result
                    if username == name[:-1]:
                        write_newline = False
                        if current_score < score:
                            line = line.replace(str(current_score), str(score))

                modified_lines.append(line)  # Add the line to modified_lines

        if write_newline:
            modified_lines.append(name[:-1] + " " + str(score) + "\n")

        with open("scores.txt", "w") as write_file:
            write_file.writelines(modified_lines)

    rank = 1
    with open("scores.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            result = extract_username_and_score(line)
            if result:
                username, current_score = result
                if current_score > score:
                    rank += 1
    pygame.draw.rect(SCREEN, (255,255,255), (0, SCREEN_HEIGHT-PLAYER_BOTTOM-14, SCREEN_WIDTH, PLAYER_BOTTOM+14))
    textSurface = font.render("You rank "+str(rank), True, (0, 0, 0))
    SCREEN.blit(textSurface, (5, SCREEN_HEIGHT-PLAYER_BOTTOM-10))
    pygame.display.update()
    time.sleep(1)

    print("Scoreboard:")
    with open("scores.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            result = extract_username_and_score(line)
            if result:
                username, score = result
                print(f"{username} : {score}")