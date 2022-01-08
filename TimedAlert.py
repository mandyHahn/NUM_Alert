import datetime
from settings import showToast
import threading
from Alert import Alert

class TimedAlert:
    def __init__(self, notificationDuration, title, message, time):
        self.notificationDuration = notificationDuration
        self.title = title
        self.message = message
        self.alert = Alert(title, message, notificationDuration)
        self.time = time
        self.startMinute = datetime.datetime.now().minute
        self.timer = threading.Timer(1, self.setupTimer)
        self.timer.start()

    def setupTimer(self):
        if not datetime.datetime.now().minute == self.startMinute:
            self.checkTimer()
        else:
            self.timer = threading.Timer(1, self.setupTimer)
            self.timer.start()

    def checkTimer(self):
        tempTime = datetime.datetime.now()
        if self.time.hour == tempTime.hour and self.time.minute == tempTime.minute:
            showToast(self.alert.title, self.alert.message, self.alert.notificationDuration)
        self.timer = threading.Timer(60, self.checkTimer)
        self.timer.start()
