import pygame, sys
from pygame.locals import *


pygame.init()

# COLORS
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((600,800))
pygame.display.set_caption('Mito Pong!')
clock = pygame.time.Clock()

# rectX, rectY = 250, 745
# rectangle = pygame.Rect(250, 745, 100, 10)
rectangleX, rectangleY = 250, 745
ballX, ballY = 300,300

velX = 5
ballVelX, ballVelY = 5, 5

# enemies
# eneX, eneY = [10, 110, 210], [10, 30, 50]
# for i in range(10, 600, 110):
#     eneX.append(i)
#     eneY.append(i)

while True:
    DISPLAYSURF.fill(WHITE)
    
    # pygame.draw.rect(DISPLAYSURF,(180,70,70), rectangle)
    rectangle = pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (rectangleX, rectangleY, 100, 10))
    ball = pygame.draw.circle(DISPLAYSURF, (125, 245, 62), (ballX, ballY), 10)

    # drawing enemies
    # for i in eneX:
    #     for i in eneY:
    #         pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (eneX[i], eneY[i], 100, 10))
    enemies = [
        pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (10, 10, 100, 10)),
        pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (10, 30, 100, 10))
    ]


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         rectangle.left -= velX
        #     elif event.key == pygame.K_RIGHT:
        #         rectangle.left += velX
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            rectangleX -= velX
        elif event.key == pygame.K_RIGHT:
            rectangleX += velX

    if ballY >= 810:
        ballX, ballY = 300,300
    elif ballX >= 590 or ballX <= 10:
        ballVelX *= -1
    
    if ballY <= 10:
        ballVelY *= -1
    
    #collitions
    if ball.colliderect(rectangle):
        # ballVelX *= -1
        ballVelY *= -1
    
    for i in enemies:
        if ball.colliderect(i):
            # print("die!")
            ballVelY *= -1
            enemies.remove(i)

    # ball movement
    ballX += ballVelX
    ballY += ballVelY
        

    pygame.display.update()
    clock.tick(60)