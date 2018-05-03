import threading
import time
import sys


class Thread_Animations(threading.Thread):

    def __init__(self, nam, act, pler, leng, delay=.08, joined=None):
        threading.Thread.__init__(self, target=self.run)
        self.name = nam
        self.action = act
        self.player = pler
        self.length = leng
        self.wait_Time = delay
        self.to_join = joined
        self.cancel = False


    def run(self):
        if not self.to_join == None:
            self.to_join.join()
        self.player.in_animation = True
        for i in range(1, self.length+1):
            if self.cancel:
                print('exiting')
                sys.exit()
            self.player.update(self.action, i)
            time.sleep(self.wait_Time)
        self.player.update('idle', 1)
        self.player.in_animation = False
