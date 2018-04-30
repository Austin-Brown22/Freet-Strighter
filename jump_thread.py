import threading
import time

class Jump_Thread(threading.Thread):

    def __init__(self, pler,direction):
        threading.Thread.__init__(self, target=self.run)
        self.player = pler
        self.direction = direction
        self.delay = .04
        self.height = 110
        self.refreshes = 10
        self.y_incrament = self.height/self.refreshes
        if self.player.jump_dir == 'None':
            self.x_dist = 0
        elif self.player.jump_dir == 'right':
            self.x_dist = 90
        elif self.player.jump_dir == 'left':
            self.x_dist = -90
        self.x_incrament = self.x_dist/self.refreshes

    def run(self):
        self.player.in_jump = True
        if self.direction == 'right':
            for i in range(self.refreshes):
                while self.player.is_updating:
                    time.sleep(.005)
                if not self.player.is_colliding:
                    self.player.rect.x += self.x_incrament
                self.player.rect.y -= self.y_incrament
                time.sleep(self.delay)
            for i in range(self.refreshes):
                while self.player.is_updating:
                    time.sleep(.005)
                if not self.player.is_colliding:
                    self.player.rect.x += self.x_incrament
                self.player.rect.y += self.y_incrament
                time.sleep(self.delay)
        else:
            for i in range(self.refreshes):
                while self.player.is_updating:
                    time.sleep(.005)
                if not self.player.is_colliding:
                    self.player.rect.x -= self.x_incrament
                self.player.rect.y -= self.y_incrament
                time.sleep(self.delay)
            for i in range(self.refreshes):
                while self.player.is_updating:
                    time.sleep(.005)
                if not self.player.is_colliding:
                    self.player.rect.x -= self.x_incrament
                self.player.rect.y += self.y_incrament
                time.sleep(self.delay)
        self.player.in_jump = False
