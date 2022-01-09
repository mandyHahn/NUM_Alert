class Alert:
    # Constructor
    # title - the title of the alert
    # message - The message of the alert
    # notificationTime - the time of the notification
    def __init__(self, title, message, notificationDuration):
        self.title = title
        self.message = message
        self.notificationDuration = notificationDuration
