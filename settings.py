from win10toast import ToastNotifier

toast = ToastNotifier()


def showToast(title, message, duration):
    if not toast.notification_active():
        toast.show_toast(title, message, duration=duration, threaded=True)
    else:
        print("here")
