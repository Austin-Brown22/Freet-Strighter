import pygame
import thread_animations
import thread_moving_sprites
import jump_thread
import time

class Players(pygame.sprite.Sprite):
    def __init__(self, xinit, yintit, speed, nam, number):
        pygame.sprite.Sprite.__init__(self)
        self.name = nam
        self.image_name = str(self.name) + ' Sprites\\' + str(self.name) + '_idle1.png'
        self.image = pygame.image.load(self.image_name)
        self.rect = self.image.get_rect()
        self.rect.x = xinit
        self.rect.y = yintit
        self.vel = speed
        self.player_num = number
        self.health = 100
        self.threads = []
        self.in_animation = False
        self.is_crouched = False
        self.max_health = 50
        self.cur_health = 50
        self.in_jump = False
        self.is_updating = False
        self.jump_dir = 'None'
        self.up_atck = False

    def update(self, action, num):
        self.is_updating = True
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.image = pygame.image.load(self.name + ' Sprites\\' + self.name + '_'+action+str(num)+'.png')
        self.rect.x = temp_x
        self.rect.y = temp_y
        self.is_updating = False

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

        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'jump', self, 2, .5))
        self.threads[-1].start()
        self.threads.append(jump_thread.Jump_Thread(self,'right'))
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
                if not self.in_animation and not self.in_jump:
                    self.jump()
            elif direction == 'undown':
                self.uncrouch()
            elif direction == 'i':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downpunch', self, 2))
                        self.threads[-1].start()
                    elif self.up_atck:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'uppunch', self, 3))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
                        self.threads[-1].start()
            elif direction == 'o':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downkick', self, 2))
                        self.threads[-1].start()
                    elif self.up_atck:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'upkick', self, 3))
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
                    elif self.up_atck:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'uppunch', self, 3))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'punch', self, 2))
                        self.threads[-1].start()
            elif direction == '5':
                if not self.in_animation:
                    if self.is_crouched:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'downkick', self, 2))
                        self.threads[-1].start()
                    elif self.up_atck:
                        self.threads.append(thread_animations.Thread_Animations('thread' + str(len(self.threads)), 'upkick', self, 3))
                        self.threads[-1].start()
                    else:
                        self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'kick', self, 2))
                        self.threads[-1].start()
            elif direction == '6':
                if not self.in_animation and not self.is_crouched:
                    self.threads.append(thread_animations.Thread_Animations('thread'+str(len(self.threads)), 'hadouken', self, 4))
                    self.threads[-1].start()
            elif direction == '0':
                if not self.in_animation and not self.in_jump:
                    self.jump()
