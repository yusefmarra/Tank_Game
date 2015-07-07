import pygame
from pygame.locals import *
from testtanks import *

pygame.init()
screen = pygame.display.set_mode([640, 480])
#t = Tank([50,50])
running = 1
#pygame.key.set_repeat(100, 200)
clock = pygame.time.Clock()
shells = pygame.sprite.Group()


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
    pressed = pygame.key.get_pressed()

    if pressed[K_SPACE]:
        shells.add(Shell([50,50], 150))
        #shell1 = Shell(t.turret.rect.center, t.turret.rotationCounter)
        #Shell(t.turret.rect.center, t.turret.rotationCounter).add(shells)
    
    shells.update()
    
    screen.fill([200, 200, 200])    

    shells.draw(screen)
        
    #screen.blit(t.image, t.rect)
    #screen.blit(t.turret.image, t.turret.rect)
    
    pygame.display.update()
    #pygame.display.flip()
    