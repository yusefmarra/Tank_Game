import os, sys
import pygame
from pygame.locals import *


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
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

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





class Cow(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('cow.bmp', -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_pos
        self.shot = 0
    def update(self):
        if self.shot:
            self.die()
    def die():
        while self.rect.bottom < 480:
            self.rect.bottom += 10
        self.kill()
        


class Cross(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = load_image('cross.bmp', -1)
        self.rect = self.image.get_rect()
        self.shooting = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shooting:
            self.rect.move_ip(5, 10)

    def shoot(self, targets):
        "returns the target that's hit"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            for target in targets:
                if hitbox.colliderect(target.rect):
                    return target
                else:
                    return false

def main():
    pygame.init()
    pygame.mouse.set_visible(0)
    background = 'SH_background.bmp'
    screen = Screen(background)
    cross = Cross()
    cows = pygame.sprite.RenderUpdates()
    
    for location in [[550, 400],
                    [200, 380],
                    [300, 290]]:
        cows.add(Cow(location))
    cows.add(cross)
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0
            elif event.type == QUIT:
                running = 0
        cows.update()
        cowRects = cows.draw(screen.screen)
        #cross.update()
        pygame.display.update(cowRects)
        cows.clear(screen.screen, screen.background)
    sys.exit()
    
if __name__ == '__main__': main()
