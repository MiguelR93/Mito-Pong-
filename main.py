import pygame, sys
from pygame.locals import *


pygame.init()

# COLORS
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((600,800))
pygame.display.set_caption('Mito Pong!')

# rectX, rectY = 250, 745
rectangle = pygame.Rect(250, 745, 100, 10)
circle = (300,735)

velX, velY = 5, 5

while True:
    DISPLAYSURF.fill(WHITE)
    
    pygame.draw.rect(DISPLAYSURF,(180,70,70), rectangle)
    pygame.draw.circle(DISPLAYSURF, (125, 245, 62), circle, 10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

        if pygame.key.get_pressed()[K_RIGHT]:
            print("A la derecha")
            rectangle.left += velX
            # rectangle.left = rectX
        elif pygame.key.get_pressed()[K_LEFT]:
            print("A la izquierda")
            rectangle.left -= velX
            # rectangle.left = rectX
    
    if circle.colliderect(rectangle):
        # invierte la dirección de la pelota
        


    pygame.display.update()