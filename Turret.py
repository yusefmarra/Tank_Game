import pygame
from pygame.locals import *
from load_images import *

class Turret(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.images = load_images(['Turret1.bmp', 'Turret2.bmp', 'Turret3.bmp', 'Turret4.bmp'], -1)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos
        self.rotationCounter = 360
    def update(self, center, input = ''):
        if input == 'tRight' or input == 'tLeft':
            self._rotate(input)
        self.rect.center = center
    def _rotate(self, direction):
        #Track the amount of rotation
        if direction == 'tRight':
            self.rotationCounter += 30
        elif direction == 'tLeft':
            self.rotationCounter -=30
        
        #Display the proper images based on the position of the rotation counter
        if self.rotationCounter == 360 or self.rotationCounter == 0:
            self.image = self.images[0]
        elif self.rotationCounter == 30 or self.rotationCounter > 360:
            self.image = self.images[1]
        elif self.rotationCounter == 60:
            self.image = self.images[2]
        elif self.rotationCounter == 90:
            self.image = self.images[3]
        elif self.rotationCounter == 120:
            self.image = pygame.transform.flip(self.images[2], 0, 1)
        elif self.rotationCounter == 150:
            self.image = pygame.transform.flip(self.images[1], 0, 1)
        elif self.rotationCounter == 180:
            self.image = pygame.transform.flip(self.images[0], 0, 1)
        elif self.rotationCounter == 210:
            self.image = pygame.transform.flip(self.images[1], 1, 1)
        elif self.rotationCounter == 240:
            self.image = pygame.transform.flip(self.images[2], 1, 1)
        elif self.rotationCounter == 270:
            self.image = pygame.transform.flip(self.images[3], 1, 0)
        elif self.rotationCounter == 300:
            self.image = pygame.transform.flip(self.images[2], 1, 0)
        elif self.rotationCounter == 330 or self.rotationCounter < 0:
            self.image = pygame.transform.flip(self.images[1], 1, 0)
    def _shoot(self):
        pass