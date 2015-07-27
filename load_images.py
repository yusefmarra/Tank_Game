import pygame
import os, sys
from pygame.locals import *

def load_images(names, colorkey=None):
    images = []
    for name in names:
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except:
            print 'Cannot load image:', name
            raise pygame.error(message)
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((5,5))
            image.set_colorkey(colorkey, RLEACCEL)
        images.append(image)
    return images

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((5,5))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
