import sys
import csv
from qtpy import QtWidgets

from ui_pcdaten.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_pcdaten = Ui_MainWindow()
        self.ui_pcdaten.setupUi(self)


window = MainWindow()

window.show()

sys.exit(app.exec_())

