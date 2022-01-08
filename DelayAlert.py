import threading
from Alert import Alert
from settings import showToast


class DelayAlert:
    # Constructor
    # timeBetweenInterval - The time between the intervals of the function
    # alert - What alert to trigger
    # title - The title of the notification
    # message - Message to display
    def __init__(self, timeBetweenInterval, notificationDuration, title, message):
        self.timeBetweenInterval = timeBetweenInterval
        self.notificationTime = notificationDuration
        self.alert = Alert(title, message, notificationDuration)
        self.timer = threading.Timer(self.timeBetweenInterval, self.performEvent)
        self.timer.start()

    # Perform the event and create a new timer
    def performEvent(self):
        showToast(self.alert.title, self.alert.message, self.alert.notificationDuration)
        self.timer = threading.Timer(self.timeBetweenInterval, self.performEvent)
        self.timer.start()
