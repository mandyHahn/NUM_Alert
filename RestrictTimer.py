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
        # call the event
        kill_unwanted(exeList)
        # initialize the timer that will run once every timeBetweenInterval seconds, and then calls performEvent
        # which calls function kill_unwanted, and supply event with exeList
        self.timer = threading.Timer(self.timeBetweenInterval, self.performEvent, args=[exeList])
        # start the initialized timer
        self.timer.start()
