import threading
import time


class thread_Moving_Sprites(threading.Thread):

    def __init__(self, name, dX, dY, period, pler, joined=None):
        threading.Thread.__init__(self, target=self.run)
        self.x_vel = (dX)/period
        self.y_vel = dY/period
        self.period = period
        self.name = name
        self.player = pler
        self.to_join = joined



    def run(self):
        if not self.to_join == None:
            print('join')
            self.to_join.join()

        print('start')
        for i in range(self.period):
            print(self.player.rect.y)
            self.player.rect.x += self.x_vel
            self.player.rect.y += self.y_vel
            print(self.player.rect.y)
            time.sleep(.3)
        print('end')