import threading
import time


class thread_Moving_Sprites(threading.Thread):

    def __init__(self, name, dX, dY, period, pler):
        threading.Thread.__init__(self, target=self.run)
        self.deltaX = dX
        self.deltaY = dY
        self.time = period
        self.name = name
        self.player = pler