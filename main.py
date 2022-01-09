from PyQt5 import QtCore, QtGui, QtWidgets, uic
from DelayAlert import DelayAlert
from TimedAlert import TimedAlert
import datetime


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('GUI.ui', self)
        MainWindow.delayAlerts = []
        MainWindow.timedAlerts = []
        MainWindow.numDelayAlerts = 0
        MainWindow.numTimedAlerts = 0

    def delete_alert(self, timerList, guiList, index):
        timerList[index].timer.cancel()
        del timerList[index]
        guiList.takeItem(index)

    def delete_selected_timedAlert(self):
        self.delete_alert(self.timedAlerts, self.currentTimedAlertsList, self.currentTimedAlertsList.currentRow())
        self.numTimedAlerts -= 1

    def delete_selected_delayAlert(self):
        self.delete_alert(self.delayAlerts, self.currentDelayAlertsList, self.currentDelayAlertsList.currentRow())
        self.numDelayAlerts -= 1

    def add_delayAlert(self):
        self.delayAlerts.append(
            DelayAlert(self.frequencyDurationSpinbox.value(), self.notificationDurationSpinbox.value(),
                       self.alertTypeCombobox.currentText(), self.customMessageField.text() + " "))

        self.currentDelayAlertsList.insertItem(self.numDelayAlerts, self.alertTypeCombobox.currentText() + ' - "' +
                                               self.customMessageField.text() + '" (' +
                                               str(self.frequencyDurationSpinbox.value()) + ' mins)')
        self.numDelayAlerts += 1

    # timeParser - Parses military time and returns it as regular time
    # hours - The hour to parse (0-23)
    # minutes - The minute to parse (0-59)
    def timeParser(self, hours, minutes):
        returnStr = ""  # Blank return string
        if hours == 12 or hours == 0:  # The hour in AMPM form is 12
            returnStr += "12:"
        else:  # Every other case
            returnStr += str(hours % 12) + ":"
        returnStr += str(minutes).zfill(2)  # Add the minutes to the string
        returnStr += " AM" if hours < 12 else " PM"  # Adds whether it is AM or PM
        return returnStr  # Return the string

    def add_timedAlert(self):
        # print("here" + self.selectTimeBox.time().toPyDateTime() )
        enteredHour = self.selectTimeBox.time().hour()
        enteredMinute = self.selectTimeBox.time().minute()
        currDate = datetime.datetime.now()
        convertedDate = datetime.datetime(currDate.year, currDate.month, currDate.day,
                                          self.selectTimeBox.time().hour(), self.selectTimeBox.time().minute())


        self.timedAlerts.append(
            TimedAlert(self.notificationDurationSpinbox_2.value(), self.alertTypeCombobox_2.currentText(),
                       self.customMessageField_2.text() + " ", convertedDate))

        self.currentTimedAlertsList.insertItem(self.numTimedAlerts, self.alertTypeCombobox_2.currentText() + ' - "' +
                                               self.customMessageField_2.text() + '" (' +
                                               self.timeParser(enteredHour, enteredMinute) + ')')
        self.numTimedAlerts += 1

    def closeEvent(self, event):
        for t in self.alerts:
            t.timer.cancel()
        event.accept()  # let the window close


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
