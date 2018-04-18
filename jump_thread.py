import threading
import time

class Jump_Thread(threading.Thread):

    def __init__(self, pler,direction):
        threading.Thread.__init__(self, target=self.run)
        self.player = pler
        self.direction = direction

    def run(self):
        if self.direction == 'right':
            pass

