import threading
from Alert import Alert
from settings import showToast


class TimedAlert:
    # Constructor
    # timeBetweenInterval - The time between the intervals of the function
    # alert - What alert to trigger
    # title - The title of the notification
    # message - Message to display
    def __init__(self, timeBetweenInterval, notificationTime, title, message):
        self.timeBetweenInterval = timeBetweenInterval
        self.notificationTime = notificationTime
        self.alert = Alert(title, message, notificationTime)
        self.timer = threading.Timer(self.timeBetweenInterval - self.notificationTime, self.performEvent)
        self.timer.start()

    # Create a timer for the given event
    def createTimer(self):
        self.timer = threading.Timer(self.timeBetweenInterval - self.notificationTime, self.performEvent)
        self.timer.start()

    # Perform the event and create a new timer
    def performEvent(self):
        showToast(self.alert.title, self.alert.message, self.alert.notificationTime)
        self.createTimer()

