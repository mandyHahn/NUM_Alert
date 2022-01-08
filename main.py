from PyQt5 import QtCore, QtGui, QtWidgets, uic
from TimedAlert import TimedAlert


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('GUI.ui', self)
        MyWindow.alerts = []
        MyWindow.numAlerts = 0

    def delete_alert(self, index):
        self.alerts.pop(index)
        self.currentAlertsList.takeItem(index)

    def add_alert(self):
        self.alerts.append(TimedAlert(self.frequencyDurationSpinbox.value(), self.notificationDurationSpinbox.value(),
                                      self.alertTypeCombobox.currentText(), self.customMessageField.text()))
        window.currentAlertsList.insertItem(self.numAlerts, self.alertTypeCombobox.currentText() + '"' +
                                            self.customMessageField.text() + '" (' +
                                            self.frequencyDurationSpinbox.value() + ' mins)')
        self.numAlerts += 1

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    # window.tableWidget.setRowCount(4)
    for x in range(40):
        window.currentAlertsList.insertItem(x, "test" + str(x))
        window.alerts.append(x)
        # item = QtWidgets.QTableWidgetItem()
        # item.setText("blah blah")
        # window.tableWidget.setItem(1, x, item)
    print(window.alerts)
    window.delete_alert(10)
    print(window.alerts)

    # _translate = QtCore.QCoreApplication.translate
    # item = QtWidgets.QTableWidgetItem()
    # item = window.tableWidget.item(1, 0)
    # item.setText(_translate("Form", "Parwiz"))
    # item = window.tableWidget.item(1, 1)
    # item.setText(_translate("Form", "par@gmail.com"))
    # item = window.tableWidget.item(1, 2)
    # item.setText(_translate("Form", "5656565"))
    window.show()
    sys.exit(app.exec_())
