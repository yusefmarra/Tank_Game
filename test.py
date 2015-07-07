import pygame
from pygame.locals import *
from testtanks import Tank

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('Tank Game')

t = Tank([50,50])
running = 1
#pygame.key.set_repeat(100, 200)
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((200, 200, 200))


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0
    pressed = pygame.key.get_pressed()

    
    
    t.update(pressed)


    screen.blit(background, (0, 0))

    t.turret.shells.update()


    if t.turret.isFlashing:
        t.turret.shells.draw(screen)
        screen.blit(t.turret.flash, t.turret.flash.get_rect(center = t.turret.rect.center))
        t.turret.isFlashing = 0
    elif t.turret.flash and t.turret.isFlashing == 0:
        screen.blit(background, t.turret.flash.get_rect(center = t.turret.rect.center))    
        t.turret.shells.draw(screen)

    screen.blit(t.image, t.rect)
    screen.blit(t.turret.image, t.turret.rect)

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(str(t.turret.rotationCounter), 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width()/2)
        screen.blit(text, textpos)    
    
    
    pygame.display.update()
    
    #pygame.display.flip()
    