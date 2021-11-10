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
ballX, ballY = 300,350

velX = 5
ballVelX, ballVelY = 5, 5

# enemies
# eneX, eneY = [10, 110, 210], [10, 30, 50]
# for i in range(10, 600, 110):
#     eneX.append(i)
#     eneY.append(i)
eneX = list(range(10, 500, 110))
eneY = list(range(50, 300, 30))

enemy = []
PLAYERPOINTS = 0
LIFES = 5
for i in eneX:
    for e in eneY:
        enemy.append((i, e, 100, 10))

#Savage Text
myFont = pygame.font.SysFont("Arial", 30)

# Game status
playerStatusWon = None

while True:
    DISPLAYSURF.fill(WHITE)
    
    # pygame.draw.rect(DISPLAYSURF,(180,70,70), rectangle)
    rectangle = pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (rectangleX, rectangleY, 100, 10))
    ball = pygame.draw.circle(DISPLAYSURF, (125, 245, 62), (ballX, ballY), 10)

    #mesage
    totalPoints = myFont.render(f"Has hecho: {PLAYERPOINTS}", 0, (0,0,0))
    DISPLAYSURF.blit(totalPoints, (10, 10))
    lifesRemaining = myFont.render(f"Vidas: {LIFES}", 0, (0,0,0))
    DISPLAYSURF.blit(lifesRemaining, (450, 10))

    


    # drawing enemies
    # for i in eneX:
    #     for i in eneY:
    #         pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (eneX[i], eneY[i], 100, 10))
    # enemies = [
    #     pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (10, 10, 100, 10)),
    #     pygame.draw.rect(DISPLAYSURF, (180, 70, 70), (10, 30, 100, 10))
    # ]

    for i in enemy:
        pygame.draw.rect(DISPLAYSURF, (180, 70, 70), i)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         rectangle.left -= velX
        #     elif event.key == pygame.K_RIGHT:
        #         rectangle.left += velX
    
    if playerStatusWon == True:
        DISPLAYSURF.fill(WHITE)
        youWin = myFont.render("Ganaste!", 0, (0,0,0))
        DISPLAYSURF.blit(youWin, (250, 400))
    elif playerStatusWon == False:
        DISPLAYSURF.fill(WHITE)
        youLose = myFont.render("Perdiste!", 0, (0,0,0))
        DISPLAYSURF.blit(youLose, (250, 400))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if rectangleX <= 0:
                rectangleX += 0
            else:    
                rectangleX -= velX
        elif event.key == pygame.K_RIGHT:
            if rectangleX >500:
                rectangleX += 0
            else: 
                rectangleX += velX

    if ballY >= 810:
        ballVelX *= -1
        ballX, ballY = 300,350
        LIFES -= 1
    elif ballX >= 590 or ballX <= 10:
        ballVelX *= -1
    
    if ballY <= 10:
        ballVelY *= -1
    
    #collitions
    if ball.colliderect(rectangle):
        # ballVelX *= -1
        ballVelY *= -1
    
    for i in enemy:
        if ball.colliderect(i):
            # print("die!")
            ballVelY *= -1
            enemy.remove(i)
            PLAYERPOINTS += 1

    if len(enemy) == 0:
        playerStatusWon = True
    elif LIFES == 0:
        playerStatusWon =False

    if playerStatusWon == True:
        print("Ganaste!")
        # break
    elif playerStatusWon == False:
        print("Perdiste")
        # break

    # ball movement
    ballX += ballVelX
    ballY += ballVelY
        

    pygame.display.update()
    clock.tick(60)

