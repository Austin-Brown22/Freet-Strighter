import pygame
import thread_animations
import thread_moving_sprites


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
        self.health = 100
        self.threads = []
        self.in_animation = False
        self.is_crouched = False

    def update(self, action, num):
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
        #self.in_animation = True
        self.is_crouched = True

    def uncrouch(self):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites/' + self.name + '_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y
        #self.in_animation = False
        self.is_crouched = False

    # go through jump animation and du de stuph
    def jump(self):
        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'jump', self, 2, .2))
        self.threads[-1].start()
        self.threads.append(thread_moving_sprites.thread_Moving_Sprites('thread' + str(len(self.threads)),50,-50,1,self))
        self.threads[-1].start()
        # do a .join so that the secound move tghread starts after the first move thread or dont
        self.threads.append(thread_moving_sprites.thread_Moving_Sprites('thread' + str(len(self.threads)), 50, 50, 1, self, self.threads[-1]))
        self.threads[-1].start()

    def move(self, direction):
        if self.name == 'ken':
            if direction == 'd':
                if not (self.in_animation or self.is_crouched):
                    self.rect.x += self.vel
            elif direction == 'a':
                if not (self.in_animation or self.is_crouched):
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
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downpunch', self, 2))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
                        self.threads[-1].start()
            elif direction == 'o':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downkick', self, 2))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'kick', self, 2))
                        self.threads[-1].start()
            elif direction == 'p':
                if not self.in_animation and not self.is_crouched:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'hadouken', self, 4))
                    self.threads[-1].start()
        else:
            if direction == 'right':
                if not (self.in_animation or self.is_crouched):
                    self.rect.x += self.vel
            elif direction == 'left':
                if not (self.in_animation or self.is_crouched):
                    self.rect.x -= self.vel
            elif direction == 'down':
                self.crouch()
            elif direction == 'up':
                pass
            elif direction == 'undown':
                self.uncrouch()
            elif direction == '4':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downpunch', self, 2))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
                        self.threads[-1].start()
            elif direction == '5':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downkick', self, 2))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'kick', self, 2))
                        self.threads[-1].start()
            elif direction == '6':
                if not self.in_animation and not self.is_crouched:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'hadouken', self, 4))
                    self.threads[-1].start()
            elif direction == '0':
                self.jump()
