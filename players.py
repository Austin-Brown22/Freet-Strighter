import pygame
import sys


class Players(pygame.sprite.Sprite):

    def __init__(self, xinit, yintit, speed, nam):
        # pygame.sprite.Sprite.__init__(self)
        self._Sprite__g = []
        self.name = nam
        self.image = pygame.image.load(self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit
        self.vel = speed

    def update(self):#need to make this work before i can actually test anything
        pass

    # change image and update self.rect
    def crouch(self):
        self.image = pygame.image.load('ryu_crouch.png')
        self.rect = self.image.get_rect()

    # go through jump animation and du de stuph
    def jump(self):
        pass

    def move(self, direction):
        if direction == 'right':
            self.x += self.vel
        elif direction == 'left':
            self.y -= self.vel
        elif direction == 'down':
            self.crouch()
        elif direction == 'up':
            self.jump()



