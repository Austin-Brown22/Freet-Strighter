import pygame
import sys
class Players:
    image = pygame.image.load('ryu_idle1.jpeg')#temp filename till wess gets his shit together
    def __init__(self, xinit, yintit, speed):
        #pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit
        self.vel = speed

    #change image and update self.rect
    def crouch(self):
        image = pygame.image.load('ryu_crouch.jpeg')
        self.rect = self.image.get_rect()

    def jump(self):
        pass

    def move(self, dir):
        if dir == 'right':
            self.x += self.vel
        elif dir == 'left':
            self.y -= self.vel
        elif dir == 'down':
            self.crouch()
        elif dir == 'up':
            self.jump()