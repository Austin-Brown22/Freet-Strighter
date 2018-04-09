import pygame
import sys

#C:\Users\b0503447\PycharmProjects\Freet-Strighter\ken Sprites\ken_idle1.png
class Players(pygame.sprite.Sprite):

    def __init__(self, xinit, yintit, speed, nam,number):
        pygame.sprite.Sprite.__init__(self)
        self.name = nam
        self.image = pygame.image.load(self.name + ' Sprites\\' + self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit
        self.vel = speed
        self.player_num = number

    def update(self):#need to make this work before i can actually test anything
        pass

    # change image and update self.rect
    def crouch(self):
        self.image = pygame.image.load('ryu_crouch.png')
        self.rect = self.image.get_rect()

    def uncrouch(self):
        self.image = pygame.image.load('ryu_idle1.png')
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
        elif direction == 'undown':
            self.uncrouch()
