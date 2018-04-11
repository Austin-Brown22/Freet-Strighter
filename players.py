import pygame
import thread_animations


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
        self.health = 100
        self.threads = []
        self.in_animation = False

    def update(self, action, num):
        print('updating to sprite num' + str(num))
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites\\' + self.name + '_'+action+str(num)+'.png')
        self.rect.x = temp_x
        self.rect.y = temp_y

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
                pass
            elif direction == 'space':
                self.jump()
            elif direction == 'undown':
                self.uncrouch()
            elif direction == 'i':
                print('pressed i')
                if not self.in_animation:
                    print('calling thread')
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
            elif direction == 'o':
                if not self.in_animation:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'kick', self, 2))
            elif direction == 'p':
                if not self.in_animation:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'hadouken', self, 4))
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
                pass
            elif direction == 'undown':
                self.uncrouch()
            elif direction == '4':
                if not self.in_animation:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
            elif direction == '5':
                if not self.in_animation:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'kick', self, 2))
            elif direction == '6':
                if not self.in_animation:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'hadouken', self, 4))
            elif direction == '0':
                self.jump()
