from win10toast import ToastNotifier
import threading

toast = ToastNotifier()


# showToast - Displays the notification (purpose - Only need 1 toaster)
# title - The title of the alert
# message - The message to be displayed to the screen
# duration - The duration of the message
def showToast(title, message, duration):
    if not toast.notification_active():  # If the toaster is not currently in use
        toast.show_toast(title, message, duration=duration, threaded=True)  # Display the notification
    else:
        t = threading.Timer(1, showToast, args=[title, message, duration])  # Wait for toaster to be clear
        t.start()  # Start the timer to wait for the toaster
