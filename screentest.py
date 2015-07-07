import os, sys
import pygame
from pygame.locals import *
from load_images import *



class Screen(object):
    def __init__(self, background, width = 640, height = 480):
        self.width, self.height = width, height
        #self.background = background
        self.screen = pygame.display.set_mode([width, height])
        
        self.background = load_image(background, -1)
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        
        
    def update(self, drawRects = [], clearRects = []):
        self.screen.blit(self.background, (0,0))
        if drawRects:
            self.draw(drawRects)
        if clearRects:
            self.clear(clearRects)
    def draw(self, rects):
        self.screen.update(rects)
        
    def clear(self, rects):
        pass 