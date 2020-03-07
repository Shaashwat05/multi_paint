import socket
import sys
import threading
import time
from queue import Queue
import pygame
import pickle
import numpy as np
import cv2
from pickle import loads,dumps

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []
count = 0



pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("paint_server")

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




def create_socket():
    try:
        global host
        global s
        global port
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as mag:
        print("socket creation error", str(mag))


def bind_socket():
    try:
        global host
        global s
        global port

        print("binding the socket")
        s.bind((host, port))
        s.listen(5)


    except socket.error as mag:
        print("socket binding error ", str(mag), " retrying")
        bind_socket()





def accepting_connection():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)
            all_connections.append(conn)
            all_address.append(address)
            print("connection has been established", address[0])

        except:
            print("error accepting connections")


def start_turtle():
    while (True):
        cmd = input()
        if (cmd == "quit"):
            for conn in all_connections:
                conn.close()
            s.close()
            sys.exit()
        if(cmd == 'start'):
            pixelarr = pygame.surfarray.array3d(screen)
            paint = True
            while paint:
                for con in all_connections:
                    con.send(dumps(pixelarr))
                    pixelarr = loads(con.recv(40960000))
                    cv2.imwrite("img.png",pixelarr)
                    print('hi')
                    #if()
    s.close()











''' def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)

        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "    " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients-----", "\n", results)


def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]

        print("you are now connected to", str(all_address[target][0]))
        print(str(all_address[target][0]), ">", end="")
        return conn

    except:
        print("selection not valid")
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if (cmd == "quit"):
                break
            if (len(str.encode(cmd)) > 0):
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("error sending command")
            break'''


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while (True):
        x = queue.get()
        if (x == 1):
            create_socket()
            bind_socket()
            accepting_connection()

        if (x == 2):
            start_turtle()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()
