from PyQt5 import QtWidgets, uic

from COVIDAlert import COVIDAlert
from DelayAlert import DelayAlert
from TimedAlert import TimedAlert
from RestrictTimer import RestrictTimer
from restrict import *
import datetime


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):                         # initialize the GUI
        super(MainWindow, self).__init__()
        uic.loadUi('GUI.ui', self)

        MainWindow.delayAlerts = []     # list of alerts of type delay
        MainWindow.timedAlerts = []     # list of alerts of type timed
        MainWindow.numDelayAlerts = 0   # the total number of delayed alerts
        MainWindow.numTimedAlerts = 0   # the total number of timed alerts

        # the following four lines keep track of the currently selected line for each of the list widgets in the GUI
        # this allows the selected line to be set to -1
        self.selectedDelayRow = -1
        self.selectedTimedRow = -1
        self.selectedRestrictRow = -1
        self.selectedAppRow = -1

        MainWindow.namesList = []   # ordered list will be used to keep track of all the apps. will be populated via InstalledApp.name
        MainWindow.toKill = []      # combobox selected items will go into this list

        MainWindow.exeDict = {}  # hashmap of name->list of executables
        MainWindow.exeList = []  # after toShutdown list was given, merge all lists matching items in toShutdown

        self.restrictTime = None    # local instance of the restrict timer (checks if any banned applications are opened every minute)
        self.covidTimer = None      # local instance of the covid cases timer (gives covid case data alerts)

        setup_apps(self.namesList, self.exeDict)    # load all applications in the user's system that can be banned

        self.namesList.sort()           # sort the applications so they display alphabetically

        for name in self.namesList:     # add each application to the GUI list
            self.applicationsList.addItem(name)

    # delete_alert: deletes the alert at the given index from all lists
    # timerList - the local instance list to delete the alert from
    # guiList - the displayed gui list widget to delete the alert from
    # index - the index of the alert to be deleted
    # totalNum - the total number of alerts in both lists (for error checking)
    def delete_alert(self, timerList, guiList, index, totalNum):
        if index < 0 or index >= totalNum:              # throw an error if the index is out of bounds
            raise IndexError("no selected element")

        guiList.takeItem(index)                         # otherwise remove the alert from the guiList
        timerList[index].timer.cancel()                 # stop the timer that runs the alert
        del timerList[index]                            # remove the alert from the timerList

    # delete_selected_timedAlert: run by the GUI to delete the user's selected timed alert
    def delete_selected_timedAlert(self):
        try:        # catch the error delete_alert throws, if it occurs
            self.delete_alert(self.timedAlerts, self.currentTimedAlertsList, self.selectedTimedRow, self.numTimedAlerts)
            self.numTimedAlerts -= 1

            if self.selectedTimedRow == self.numTimedAlerts:    # if the deleted alert was the last one, decrement the selected row
                self.selectedTimedRow -= 1

        except IndexError:
            pass    # do nothing

    # delete_selected_delayAlert: run by the GUI to delete the user's selected delay alert
    def delete_selected_delayAlert(self):
        try:        # catch the error delete_alert throws, if it occurs
            self.delete_alert(self.delayAlerts, self.currentDelayAlertsList, self.selectedDelayRow, self.numDelayAlerts)
            self.numDelayAlerts -= 1
            if self.selectedDelayRow == self.numDelayAlerts:    # if the deleted alert was the last one, decrement the selected row
                self.selectedDelayRow -= 1

        except IndexError:
            pass    # do nothing

    # add_delayAlert: collects the user's inputted data to create a new delay alert
    def add_delayAlert(self):
        # first create a new DelayAlert object and add it to our local list
        self.delayAlerts.append(DelayAlert(self.frequencyDurationSpinbox.value()*60,
                                           self.notificationDurationSpinbox.value(),
                                           self.alertTypeCombobox.currentText(),
                                           self.customMessageField.text() + " "))

        # then add a description for the created alert to the gui
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

    def add_to_banned(self):
        numRows = self.applicationsList.count()
        try:
            if self.selectedAppRow < 0 or self.selectedAppRow >= numRows:
                raise IndexError("selection out of bounds")

            itemName = self.applicationsList.takeItem( self.selectedAppRow ).text()
            self.bannedApplicationsList.addItem(itemName)
            self.toKill.append(itemName)
            self.exeList += self.exeDict[itemName]

            if self.selectedAppRow == numRows-1:
                self.selectedAppRow -= 1

        except IndexError:
            print("app indexerror") # TODO make all error messages pass

    def unban_selected(self):
        numRows = self.bannedApplicationsList.count()
        try:
            if self.selectedRestrictRow < 0 or self.selectedRestrictRow >= numRows:
                raise IndexError("selection out of bounds")

            itemName = self.bannedApplicationsList.takeItem(self.selectedRestrictRow).text()
            self.toKill.remove(itemName)
            for item in self.exeDict[itemName]:
                self.exeList.remove(item)
            self.applicationsList.addItem(itemName)

            if self.selectedRestrictRow == numRows-1:
                self.selectedRestrictRow -= 1

        except IndexError:
            print("banned indexerror")

    def closeEvent(self, event):
        for t in self.delayAlerts:
            t.timer.cancel()
        for t in self.timedAlerts:
            t.timer.cancel()
        if self.focusModeCheckbox.isChecked():
            self.restrictTime.timer.cancel()
        if self.covidAlertsRadiobutton.isChecked():
            self.covidTimer.timer.cancel()

        event.accept()  # let the window close

    def set_selected_delayAlert(self):
        self.selectedDelayRow = self.currentDelayAlertsList.currentRow()

    def set_selected_timedAlert(self):
        self.selectedTimedRow = self.currentTimedAlertsList.currentRow()

    def set_selected_app(self):
        self.selectedAppRow = self.applicationsList.currentRow()

    def set_selected_restriction(self):
        self.selectedRestrictRow = self.bannedApplicationsList.currentRow()

    def focus_toggle(self):
        if self.focusModeCheckbox.isChecked():
            self.restrictTime = RestrictTimer(60, self.exeList)
        else:
            self.restrictTime.timer.cancel()

    def covid_toggle(self):
        if self.covidAlertsRadiobutton.isChecked():
            self.covidTimer = COVIDAlert(self.covidNotificationDurationSpinbox.value(),
                                         self.covidNotifyFrequencySpinbox.value()*60) 
            self.covidTimer.createTimer(self.covidCountryCombobox.currentText())
        else:
            self.covidTimer.timer.cancel()

    def covid_country_changed(self):
        if self.covidAlertsRadiobutton.isChecked():
            self.covidTimer.timer.cancel()
            self.covidTimer.createTimer(self.covidCountryCombobox.currentText())

    def covid_notify_change(self):
        if self.covidAlertsRadiobutton.isChecked():
            self.covidTimer.timer.cancel()
            self.covidTimer.notificationDuration = self.covidNotificationDurationSpinbox.value()
            self.covidTimer.timeBetweenAlert = self.covidNotifyFrequencySpinbox.value()
            self.covidTimer.createTimer(self.covidCountryCombobox.currentText())


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())





