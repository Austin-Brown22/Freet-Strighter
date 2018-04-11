import pygame


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
        self.is_crouched = False

    # change image and update self.rect *PROBLY SHOULDENT CROUCH MID JUMP*
    def crouch(self):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites/' + self.name + '_crouch1.png')
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y
        self.is_crouched = True

    def uncrouch(self):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites/' + self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y
        self.is_crouched = False

    # go through jump animation and du de stuph
    def jump(self):
        pass

    #  have the crouched versions in an if *ALSO HAVE A JUMPING VERSION*
    #  find a way to disallow movement while an animation is going on
    def punch(self):
        pass

    def kick(self):
        pass

    def haduken(self):
        pass

    def move(self, direction):
        if self.name == 'ken':
            if direction == 'd':
                if not self.is_crouched:
                    self.rect.x += self.vel
            elif direction == 'a':
                if not self.is_crouched:
                    self.rect.x -= self.vel
            elif direction == 's':
                self.crouch()
            elif direction == 'w':
                self.jump()
            elif direction == 'undown':
                self.uncrouch()
            elif direction == 'i':
                self.punch()
            elif direction == 'o':
                self.kick()
            elif direction == 'p':
                self.haduken()
        else:
            if direction == 'right':
                if not self.is_crouched:
                    self.rect.x += self.vel
            elif direction == 'left':
                if not self.is_crouched:
                    self.rect.x -= self.vel
            elif direction == 'down':
                self.crouch()
            elif direction == 'up':
                self.jump()
            elif direction == 'undown':
                self.uncrouch()
            elif direction == '4':
                self.punch()
            elif direction == '5':
                self.kick()
            elif direction == '6':
                self.haduken()
