import threading
import time


# noinspection PyTypeChecker
class Thread_Animations(threading.Thread):

    def __init__(self, nam, act, pler, leng):
        threading.Thread.__init__(self)
        self.name = nam
        self.action = act
        self.player = pler
        self.length = leng
        print('created a thread')
        self.run()

    def run(self):
        print('thread is running')
        self.player.in_animation = True
        for i in range(1, self.length+1):
            self.player.update(self.action, i)
            time.sleep(10)
        self.player.in_animation = False