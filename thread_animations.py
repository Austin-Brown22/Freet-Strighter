import threading
import time


# noinspection PyTypeChecker
class Thread_Animations(threading.Thread):

    def __init__(self, nam, act, pler, leng):
        threading.Thread.__init__(self, target=self.run)
        self.name = nam
        self.action = act
        self.player = pler
        self.length = leng
        self.wait_Time = .08

    def run(self):
        self.player.in_animation = True
        for i in range(1, self.length+1):
            self.player.update(self.action, i)
            time.sleep(self.wait_Time)
        self.player.update('idle', 1)
        self.player.in_animation = False
