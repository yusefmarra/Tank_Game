import pygame
from pygame.locals import *
from load_images import *


class Shell(pygame.sprite.Sprite):
    def __init__(self, initial_pos, rotation):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('shell.bmp', -1)
        self.rect.center = initial_pos
        self.orientation = rotation
    def update(self):
        
        if self.orientation == 360 or self.orientation == 0:
            self.rect.move_ip(0,-15)
        elif self.orientation == 30 or self.orientation == 390:
            self.rect.move_ip(7.5,-12.9)
        elif self.orientation == 60 or self.orientation == 420:
            self.rect.move_ip(12.9,-7.5)
        elif self.orientation == 90 or self.orientation == 450:
            self.rect.move_ip(15,0)
        elif self.orientation == 120 or self.orientation == 480:
            self.rect.move_ip(12.9,7.5)
        elif self.orientation == 150 or self.orientation == 510:
            self.rect.move_ip(7.5,12.9)
        elif self.orientation == 180 or self.orientation == 540 or self.orientation == -180:
            self.rect.move_ip(0,15)
        elif self.orientation == 210 or self.orientation == -150:
            self.rect.move_ip(-7.5,12.9)
        elif self.orientation == 240 or self.orientation == -120:
            self.rect.move_ip(-12.9,7.5)
        elif self.orientation == 270 or self.orientation == -90:
            self.rect.move_ip(-15,0)
        elif self.orientation == 300 or self.orientation == -60:
            self.rect.move_ip(-12.9,-7.5)
        elif self.orientation == 330 or self.orientation == -30:
            self.rect.move_ip(-7.5,-12.9)       
        
        
        
        if self.rect.left < 0:
            self.kill()
        elif self.rect.right > 640:
            self.kill()
        if self.rect.top <= 0:
            self.kill()
        elif self.rect.bottom >= 480:
            self.kill()
class Turret(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.images = load_images(['Turret1.bmp', 'Turret2.bmp', 'Turret3.bmp', 'Turret4.bmp'], -1)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos
        self.rotationCounter = 360
        self.rotationOffset = 0
        self.isShooting = 0
        self.shells = pygame.sprite.Group()
        
    def update(self, center, rotation, input = ''):
        if input == 'tRight' or input == 'tLeft':
            self._rotate(rotation, input)
        self.rect.center = center
        self._rotate(rotation)
        if self.isShooting:
            self._shoot()
        
    def _rotate(self, rotation, direction = ''):
        #Track the offset from the chassis rotation
        if direction == 'tRight':
            self.rotationOffset += 30
        elif direction == 'tLeft':
            self.rotationOffset -=30
        self.rotationCounter = self.rotationOffset + rotation
        #Display the proper images based on the position of the rotation counter
        if self.rotationCounter == 360 or self.rotationCounter == 0:
            self.image = self.images[0]
        elif self.rotationCounter == 30 or self.rotationCounter == 390:
            self.image = self.images[1]
        elif self.rotationCounter == 60 or self.rotationCounter == 420:
            self.image = self.images[2]
        elif self.rotationCounter == 90 or self.rotationCounter == 450:
            self.image = self.images[3]
        elif self.rotationCounter == 120 or self.rotationCounter == 480:
            self.image = pygame.transform.flip(self.images[2], 0, 1)
        elif self.rotationCounter == 150 or self.rotationCounter == 510:
            self.image = pygame.transform.flip(self.images[1], 0, 1)
        elif self.rotationCounter == 180 or self.rotationCounter == 540 or self.rotationCounter == -180:
            self.image = pygame.transform.flip(self.images[0], 0, 1)
        elif self.rotationCounter == 210 or self.rotationCounter == -150:
            self.image = pygame.transform.flip(self.images[1], 1, 1)
        elif self.rotationCounter == 240 or self.rotationCounter == -120:
            self.image = pygame.transform.flip(self.images[2], 1, 1)
        elif self.rotationCounter == 270 or self.rotationCounter == -90:
            self.image = pygame.transform.flip(self.images[3], 1, 0)
        elif self.rotationCounter == 300 or self.rotationCounter == -60:
            self.image = pygame.transform.flip(self.images[2], 1, 0)
        elif self.rotationCounter == 330 or self.rotationCounter == -30:
            self.image = pygame.transform.flip(self.images[1], 1, 0)

        if self.rotationOffset < -180:
            self.rotationOffset = 150
        elif self.rotationOffset > 180:
            self.rotationOffset = -150
        
        

    def _shoot(self):
        self.shells.add(Shell(self.rect.center, self.rotationCounter))
        self.isShooting = 0

class Tank(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.images = load_images(['TankBase1.bmp','TankBase2.bmp','TankBase3.bmp','TankBase4.bmp'], -1)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos
        self.turret = Turret(initial_pos)
        self.rotationCounter = 360
        
    def update(self, input = ''):
        #move the tank
        #self.rect.move_ip((self.x_velocity, self.y_velocity))
        #Keep it inside the screen
        
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 640:
            self.rect.right = 640
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 480:
            self.rect.bottom = 480
        
        if input == 'up':
            self._move()
        elif input == 'down':
            self._reverse()
        elif input == 'right' or input == 'left':
            self._rotate(input)
        elif input == 'tLeft' or 'tRight':
            self.turret.update(self.rect.center, self.rotationCounter, input)        
        self.turret.update(self.rect.center, self.rotationCounter)
    def _move(self):
        if self.rotationCounter == 0 or self.rotationCounter == 360:
            self.rect.move_ip(0,-5)
        elif self.rotationCounter == 30:
            self.rect.move_ip(2.5,-4.3)
        elif self.rotationCounter == 60:
            self.rect.move_ip(4.3,-2.5)
        elif self.rotationCounter == 90:
            self.rect.move_ip(5,0)
        elif self.rotationCounter == 120:
            self.rect.move_ip(4.3,2.5)
        elif self.rotationCounter == 150:
            self.rect.move_ip(2.5,4.3)
        elif self.rotationCounter == 180:
            self.rect.move_ip(0,5)
        elif self.rotationCounter == 210:
            self.rect.move_ip(-2.5,4.3)
        elif self.rotationCounter == 240:
            self.rect.move_ip(-4.3,2.5)
        elif self.rotationCounter == 270:
            self.rect.move_ip(-5,0)
        elif self.rotationCounter == 300:
            self.rect.move_ip(-4.3,-2.5)
        elif self.rotationCounter == 330:
            self.rect.move_ip(-2.5,-4.3)
        

    
    def _rotate(self, direction):
        #Track the amount of rotation
        if direction == 'right':
            self.rotationCounter += 30
            self.turret.update(self.rect.center, self.rotationCounter)
        elif direction == 'left':
            self.rotationCounter -=30
            self.turret.update(self.rect.center, self.rotationCounter)
            
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
        
        #Keep it under 360
        if self.rotationCounter > 360:
            self.rotationCounter = 30
        elif self.rotationCounter < 0:
            self.rotationCounter = 330
        


    def _reverse(self):
        if self.rotationCounter == 0 or self.rotationCounter == 360:
            self.rect.move_ip(0,5)
        elif self.rotationCounter == 30:
            self.rect.move_ip(-2.5,4.3)
        elif self.rotationCounter == 60:
            self.rect.move_ip(-4.3,2.5)
        elif self.rotationCounter == 90:
            self.rect.move_ip(-5,0)
        elif self.rotationCounter == 120:
            self.rect.move_ip(-4.3,-2.5)
        elif self.rotationCounter == 150:
            self.rect.move_ip(-2.5,-4.3)
        elif self.rotationCounter == 180:
            self.rect.move_ip(0,-5)
        elif self.rotationCounter == 210:
            self.rect.move_ip(2.5,-4.3)
        elif self.rotationCounter == 240:
            self.rect.move_ip(4.3,-2.5)
        elif self.rotationCounter == 270:
            self.rect.move_ip(5,0)
        elif self.rotationCounter == 300:
            self.rect.move_ip(4.3,2.5)
        elif self.rotationCounter == 330:
            self.rect.move_ip(2.5,4.3)

    def _shoot(self):
        pass

    def stop(self):
        pass
