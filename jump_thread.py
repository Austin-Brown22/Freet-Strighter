import threading
import time

class Jump_Thread(threading.Thread):

    def __init__(self, pler,direction):
        threading.Thread.__init__(self, target=self.run)
        self.player = pler
        self.direction = direction
        self.delay = .05
        self.height = 100
        self.refreshes = 10
        self.incrament = self.height/self.refreshes

    def run(self):
        cnt = 0
        self.player.in_jump = True
        print('start--'+str(self.player.rect.y))
        if self.direction == 'right':
            for i in range(self.refreshes):
                #self.player.rect.x += 5
                self.player.rect.y -= self.incrament
                time.sleep(self.delay)
                print(self.player.rect.y)
            for i in range(self.refreshes):
                #self.player.rect.x += 5
                self.player.rect.y += self.incrament
                time.sleep(self.delay)
                print(self.player.rect.y)
        else:
            for i in range(self.refreshes):
                #self.player.rect.x -= 5
                self.player.rect.y -= self.incrament
                time.sleep(self.delay)
            for i in range(self.refreshes):
                #self.player.rect.x -= 5
                self.player.rect.y += self.incrament
                time.sleep(self.delay)
        self.player.in_jump = False
        print('end--' + str(self.player.rect.y))
