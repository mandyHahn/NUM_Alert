import atexit
from DelayAlert import DelayAlert
from TimedAlert import TimedAlert
import datetime

alerts = list()

currDate = datetime.datetime.now()
date = datetime.datetime(currDate.year, currDate.month, currDate.day, 14, 51)
timeAlert = TimedAlert(20, "Test", "test", date)


def cancelTimers():
    for t in alerts:
        t.timer.cancel()
atexit.register(cancelTimers)

