import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
playerX = 275
playerSpeed = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerSpeed = -1
            elif event.key == pygame.K_RIGHT:
                playerSpeed = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerSpeed = 0
    playerX += playerSpeed
    SCREEN.fill((0, 0, 0))
    pygame.draw.rect(SCREEN, (255, 0, 0), (playerX, 650, 50, 75))
    pygame.display.update()