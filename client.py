import socket
import os
import subprocess
import pygame
import sys
import pickle
import numpy as np
import  cv2
from pickle import loads,dumps

s=socket.socket()
host = "172.17.60.89"
port = 9999

s.connect((host, port))


pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("paint_client")

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

def draw(radius):
    drawing = True
    clr = black
    while drawing:
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
                # print(pos)
                if ((pos[0] >= 20 and pos[0] <= 35) and (pos[1] >= 110 and pos[1] <= 130)):
                    clr = white
                    # radius = 10
                if ((pos[0] >= 20 and pos[0] <= 35) and (pos[1] >= 60 and pos[1] <= 70)):
                    clr = black
                    # radius = 5
                if ((pos[0] >= 0 and pos[0] <= 800) and (pos[1] >= 0 and pos[1] <= 40)):
                    clr = screen.get_at((pos[0], pos[1]))
                    # radius=5
                drawing = False
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_w):
                    radius += 2
                if (event.key == pygame.K_s):
                    if (radius >= 2):
                        radius -= 2
    pixelarr = pygame.surfarray.array3d(screen)
    pygame.display.update()
    #surf_string = pygame.image.tostring(screen, 'RGB')
    return pixelarr

while(True):
    #print("hi")
    #surf_string = s.recv(36768)
    #screen = pygame.image.fromstring(surf_string, [800, 600], 'RGB')

    pixelarr = loads(s.recv(40960000))
    print(pixelarr)
    pygame.surfarray.blit_array(screen, pixelarr)
    pygame.display.update()
    pixelarr1 = draw(5)
    s.send(dumps(pixelarr1))


