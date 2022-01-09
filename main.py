from PyQt5 import QtWidgets
from gui import MainWindow
import sys

# needed pip installations:
# PyQt5
# selenium
# psutil
# winapps
# win10toast

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())
