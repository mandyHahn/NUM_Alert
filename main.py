from PyQt5 import QtWidgets
from gui import MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())
