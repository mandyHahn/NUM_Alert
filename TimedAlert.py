import datetime
from settings import showToast
import threading
from Alert import Alert


class TimedAlert:
    # Constructor
    # notificationDuration - The length of time the notification will be active for
    # title - The title of the alert
    # message - The message of the alert
    # time - The time at which the alert will go off.
    def __init__(self, notificationDuration, title, message, time):
        self.notificationDuration = notificationDuration
        self.title = title
        self.message = message
        self.alert = Alert(title, message, notificationDuration)
        self.time = time
        self.startMinute = datetime.datetime.now().minute
        self.timer = threading.Timer(1, self.setupTimer)
        self.timer.start()

    # setupTimer - Creates a new timer object and waits until the next full minute
    #              (eg. 12:35:00 if the program is started at 12:34:32)
    #              Then, sets the timer to go off every minute
    def setupTimer(self):
        if not datetime.datetime.now().minute == self.startMinute:  # If it's the start of a new minute
            self.checkTimer()  # Create a new timer that is called every minute
        else:
            self.timer = threading.Timer(1, self.setupTimer)  # Next second, check to see if it's a new minute
            self.timer.start()

    # checkTimer - Checks every minute whether or not it should alert the user
    def checkTimer(self):
        self.timer = threading.Timer(60, self.checkTimer)  # Check again in a minute
        self.timer.start()  # Start the new timer
        tempTime = datetime.datetime.now()  # Get current time
        if self.time.hour == tempTime.hour and self.time.minute == tempTime.minute:  # If it's the time the user wanted the alert
            showToast(self.alert.title, self.alert.message, self.alert.notificationDuration)  # Send the alert
            self.timer.cancel()  # No longer need to check, cancel the timer
