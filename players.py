import pygame
import sys


class Players(pygame.sprite.Sprite):
    def __init__(self, xinit, yintit, speed, nam, number):
        pygame.sprite.Sprite.__init__(self)
        self.name = nam
        self.image = pygame.image.load(self.name + ' Sprites\\' + self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit
        self.vel = speed
        self.player_num = number

    def update(self):  # need to make this work before i can actually test anything
        pass

    # change image and update self.rect
    def crouch(self):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites/' + self.name + '_crouch1.png')
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y

    def uncrouch(self):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites/' + self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y

    # go through jump animation and du de stuph
    def jump(self):
        pass

    def move(self, direction):
        if self.name == 'ken':
            if direction == 'd':
                self.rect.x += self.vel
            elif direction == 'a':
                self.rect.x -= self.vel
            elif direction == 's':
                self.crouch()
            elif direction == 'w':
                self.jump()
            elif direction == 'undown':
                self.uncrouch()
        else:
            if direction == 'right':
                self.rect.x += self.vel
            elif direction == 'left':
                self.rect.x -= self.vel
            elif direction == 'down':
                self.crouch()
            elif direction == 'up':
                self.jump()
            elif direction == 'undown':
                self.uncrouch()


    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
