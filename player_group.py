import pygame
import sys


class Player_Group(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def move(self,direction):
        for player in self.sprites():
            player.move(direction)