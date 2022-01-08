from win10toast import ToastNotifier


class Alert:
    # Constructor
    # title - the title of the alert
    # message - The message of the alert
    # notificationTime - the time of the notification
    def __init__(self, title, message, notificationTime):
        self.title = title
        self.message = message
        self.notificationTime = notificationTime