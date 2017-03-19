# -*- coding: utf-8 -*-


import janus
import threading
from proboty.drivers.md25 import Md25


class Controller(threading.Thread):
    def __init__(self, loop, queue):
        threading.Thread.__init__(self)
        self.loop = loop
        self.queue = queue
        self.motors = Md25()

    def run(self):
        print("Running controller thread...")

        while True:
            message = None

            try:
                message = self.queue.get_nowait()
                print("Got from queue: ", message)
            except janus.SyncQueueEmpty:
                pass

            if message == 'quit':
                self.loop.stop()
                return
                
            self.motors.drive(128, 128)
        
