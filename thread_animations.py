import threading
import time
import sys


class Thread_Animations(threading.Thread):

    def __init__(self, nam, act, pler, leng, delay=.08, joined=None,hold_time=0.0):
        threading.Thread.__init__(self, target=self.run)
        self.name = nam
        self.action = act
        self.player = pler
        self.length = leng
        self.wait_Time = delay
        self.to_join = joined
        self.hold_time = hold_time


    def run(self):
        time.sleep(self.hold_time)
        if not self.to_join == None:
            self.to_join.join()
        self.player.in_animation = True
        for i in range(1, self.length+1):
            print(self.action)
            if self.player.shtahp_thread:
                print('exiting')
                self.player.shtahp_thread = False
                self.player.in_animation = False
                raise SystemExit
            self.player.update(self.action, i)
            time.sleep(self.wait_Time)
        self.player.update('idle', 1)
        self.player.in_animation = False
