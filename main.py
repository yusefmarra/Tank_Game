import pygame
from pygame.locals import *
from tanks import Tank

pygame.init()
screen = pygame.display.set_mode([640, 480])
t = Tank([50,50])
running = 1
#pygame.key.set_repeat(100, 200)
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0
    pressed = pygame.key.get_pressed()

    if pressed[K_UP] and pressed[K_LEFT]:
        t.update('up')
        t.update('left')
    elif pressed[K_UP] and pressed[K_RIGHT]:
        t.update('up')
        t.update('right')
    elif pressed[K_DOWN] and pressed[K_LEFT]:
        t.update('down')
        t.update('left')
    elif pressed[K_DOWN] and pressed[K_RIGHT]:
        t.update('down')
        t.update('right')
    elif pressed[K_UP]:
        t.update('up')
    elif pressed[K_DOWN]:
        t.update('down')
    elif pressed[K_LEFT]:
        t.update('left')
    elif pressed[K_RIGHT]:
        t.update('right')
    if pressed[K_a]:
        t.update('tLeft')
    elif pressed[K_d]:
        t.update('tRight')
    if pressed[K_SPACE]:
        t.turret.isShooting = 1
        #shells.add(Shell(t.turret.rect.center, t.turret.rotationCounter))
        #shell1 = Shell(t.turret.rect.center, t.turret.rotationCounter)
        #Shell(t.turret.rect.center, t.turret.rotationCounter).add(shells)
    
    t.update()
    t.turret.shells.update()
    screen.fill([200, 200, 200])    
    t.turret.shells.draw(screen)
    screen.blit(t.image, t.rect)
    screen.blit(t.turret.image, t.turret.rect)
    
    rot_txt = str(t.turret.rotationCounter)
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(rot_txt, 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width()/2)
        screen.blit(text, textpos)    
    
    
    pygame.display.update()
    #pygame.display.flip()
    