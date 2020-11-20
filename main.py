import sys
# import csv
from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog

from ui_pcdaten.mainwindow import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_pcdaten = Ui_MainWindow()
        self.ui_pcdaten.setupUi(self)
        self.ui_pcdaten.pushButton.clicked.connect(self.browsefiles)

    def browsefiles(self):
        # Problem: Wie kann der Standard Suchpfad so eingestellt werden, dass er direkt in Downloads landet
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\%Username%\Downloads')
        self.ui_pcdaten.lineSearch.setText(fname[0])


window = MainWindow()

window.show()

sys.exit(app.exec_())

