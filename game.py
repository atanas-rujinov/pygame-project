import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
PLAYER_SPEED = 1
playerX = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
running = True
goingLeft = False
goingRight = False
directionPriority = ""
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
    pygame.draw.rect(SCREEN, (255, 0, 0), (playerX, 650, 50, 75))
    pygame.display.update()