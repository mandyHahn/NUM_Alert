from win10toast import ToastNotifier
import threading

toast = ToastNotifier()


def showToast(title, message, duration):
    if not toast.notification_active():
        toast.show_toast(title, message, duration=duration, threaded=True)
    else:
        t = threading.Timer(1, showToast, args=[title, message, duration])
        t.start()
