import pygame, sys
from pygame.locals import *


pygame.init()

# COLORS
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((600,800))
pygame.display.set_caption('Mito Pong!')
clock = pygame.time.Clock()

# rectX, rectY = 250, 745
rectangle = pygame.Rect(250, 745, 100, 10)
ballX, ballY = 300,300

velX = 5
ballVelX, ballVelY = 5, 5

while True:
    DISPLAYSURF.fill(WHITE)
    
    pygame.draw.rect(DISPLAYSURF,(180,70,70), rectangle)
    ball = pygame.draw.circle(DISPLAYSURF, (125, 245, 62), (ballX, ballY), 10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rectangle.left -= velX
            elif event.key == pygame.K_RIGHT:
                rectangle.left += velX
    
    if ballY >= 810:
        ballX, ballY = 300,300
    elif ballX >= 590 or ballX <= 10:
        ballVelX *= -1
    
    if ballY <= 10:
        ballVelY *= -1
    
    if ball.colliderect(rectangle):
        ballVelX *= -1
        ballVelY *= -1
    
    ballX += ballVelX
    ballY += ballVelY
    
    # if circle.colliderect(rectangle):
        # invierte la dirección de la pelota
        # pass
        

    clock.tick(60)
    pygame.display.update()