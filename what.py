import os, sys
import pygame
from pygame.locals import *
from load_images import *
from screentest import *

pygame.init()

screen = Screen()
running = 1


while running:
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0