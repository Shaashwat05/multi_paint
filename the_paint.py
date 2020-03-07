import pygame
import sys
import cv2
import numpy as np

pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("paint")

# colours
red = (255, 0, 0)
blue = (0, 0, 255)
eraser = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

# paint constants
radius = 5
length_of_square = 20
painting = True

# the pallete
screen.fill(white)
pygame.display.update()

j = 0
k = 0
for i in range(51):
    pygame.draw.rect(screen, (i * 5, 0, 0), (j, 0, length_of_square, length_of_square))
    j += 5
    k += 5
pygame.display.update()
k = 0
for i in range(51):
    pygame.draw.rect(screen, (255, i * 5, 0), (j, 0, length_of_square, length_of_square))
    j += 5
    k += 5
pygame.display.update()
k = 0
for i in range(51):
    pygame.draw.rect(screen, (255, 255, i * 5), (j, 0, length_of_square, length_of_square))
    j += 5
    k += 5
pygame.display.update()


j = 0
k = 20
for i in range(51):
    pygame.draw.rect(screen, (0, 0, i*5), (j, 20, length_of_square, length_of_square))
    j += 5
    k += 5

k = 20
for i in range(51):
    pygame.draw.rect(screen, (i*5, 0, 255), (j, 20, length_of_square, length_of_square))
    j += 5
    k += 5

k = 20
for i in range(51):
    pygame.draw.rect(screen, (255, i*5, 255), (j, 20, length_of_square, length_of_square))
    j += 5
    k += 5



pygame.draw.rect(screen, black, (10, 50, 30, 100), 1)
pygame.display.update()

brush = pygame.image.load("C://Users//SHAASHWAT//PycharmProjects//multi_paint//brush.png")
eraser = pygame.image.load("C://Users//SHAASHWAT//PycharmProjects//multi_paint//eraser.png")
brush = pygame.transform.scale(brush, (30, 30))
eraser = pygame.transform.scale(eraser, (30, 30))
screen.blit(brush, (10, 50))
screen.blit(eraser, (10, 100))
pygame.display.update()

pygame.draw.rect(screen, black, (48, 48, 702, 502), 1)
pygame.display.update()

clr = white

#print(pxaray[0,0])
while painting:
    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            playing = False
            sys.exit()
        if (event.type == pygame.MOUSEMOTION):
            pos = event.pos
            if ((pos[0] >= 59 and pos[0] <= 741) and (pos[1] >= 59 and pos[1] <= 541)):
                pygame.draw.circle(screen, clr, pos, radius)
                pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos = event.pos
            #print(pos)
            if ((pos[0] >= 20 and pos[0] <= 35) and (pos[1] >= 110 and pos[1] <= 130)):
                clr = white
                #radius = 10
            if ((pos[0] >= 20 and pos[0] <= 35) and (pos[1] >= 60 and pos[1] <= 70)):
                clr = black
                #radius = 5
            if ((pos[0] >= 0 and pos[0] <= 800) and (pos[1] >= 0 and pos[1] <= 40)):
                clr=screen.get_at((pos[0], pos[1]))
                #radius=5
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_w):
                radius += 2
            if(event.key == pygame.K_s):
                if(radius >=2):
                    radius -= 2

