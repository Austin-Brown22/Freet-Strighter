import pygame

class Name_Sprites(pygame.sprite.Sprite):
    def __init__(self, xinit, yintit,nam):
        pygame.sprite.Sprite.__init__(self)
        self.name = nam
        self.image = pygame.image.load('ui/' + self.name + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit