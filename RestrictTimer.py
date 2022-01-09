import threading
from restrict import *


class RestrictTimer:
    # Constructor
    # timeBetweenInterval - The time between the intervals of the function
    # alert - What alert to trigger
    # title - The title of the notification
    # message - Message to display
    def __init__(self, timeBetweenInterval, exeList):
        self.timeBetweenInterval = timeBetweenInterval
        self.timer = threading.Timer(timeBetweenInterval, self.performEvent, args=[exeList])
        self.timer.start()

    # Perform the event and create a new timer
    def performEvent(self, exeList):
        kill_unwanted(exeList)
        self.timer = threading.Timer(self.timeBetweenInterval, self.performEvent, args=[exeList])
        self.timer.start()
