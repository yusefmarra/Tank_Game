import pygame
from pygame.locals import *
from testtanks import Tank, TankAI
import random

pygame.init()
screen = pygame.display.set_mode([1024, 768])
pygame.display.set_caption('Tank Game')

t = Tank(screen, [50,50])
t_AI = TankAI(screen, [200,200])

player_sprites = pygame.sprite.Group()
player_sprites.add(t)

AI_sprites = pygame.sprite.Group()
AI_sprites.add(t_AI)

for i in range(50):
    AI_sprites.add(TankAI(screen, [random.randint(200, 1000),random.randint(200,700)]))

running = 1
#pygame.key.set_repeat(100, 200)
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((136, 225, 136))


while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0
    pressed = pygame.key.get_pressed()

    screen.blit(background, (0, 0))

    player_sprites.update(pressed)
    AI_sprites.update(t.turret.shells)

    if not AI_sprites:
        AI_sprites.add(TankAI(screen, [random.randint(200, 1000),random.randint(200,700)]))


    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(str(clock.get_rawtime()), 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width()/2)
        screen.blit(text, textpos)


    pygame.display.update()

    #pygame.display.flip()
