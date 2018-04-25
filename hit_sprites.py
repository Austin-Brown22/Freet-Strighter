import pygame

class Hit_Sprites(pygame.sprite.Sprite):
    def __init__(self,nam):
        pygame.sprite.Sprite.__init__(self)
        self.name = nam
        self.rect = (0,0,10,10)
